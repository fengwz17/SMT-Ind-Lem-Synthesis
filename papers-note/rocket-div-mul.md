# Rocketchip-div-mul

记录RocketChip中divider和multipiler的源码阅读理解和证明

## Div

### 关于验证中pre-condition的设置

对于有些参数，比如w, divUnroll, mulUnroll, nXpr等，但看乘除法器模块的代码对这些参数没有限制，但实际使用中这些参数的设置是满足一定的pre-condition的，目前的原则是在验证的时候对pre-condition进行合理的设置，如大于0, `divUnroll <= w`等，然后在这个范围内找有没有进一步的限制.

- 有些可能是在外部其他传入参数的地方给的限制，比如xiangshan乘法器实际上多扩展了一位，即最高两位要么同为0,要么同为1.

### 通用参数

`minLatency`:没用到，忽略
`w`: width of in1
`mulw`, `fastMulW`: 除法中由于`cfg,mulUnroll == 0`, 因此`mulw = w`, `fastMulW = false`
`count`位宽：`log2Ceil(w / divUnroll + 1)`, 如32位除法器，divUnroll等于1的时候，count位宽为6
`remainder`位宽：`2 * mulw + 2 == 2 * w + 2`

- ```scala
    /*
    * @example {{{
    * log2Up(1)  // returns 0  log2Up(2)  // returns 1
    * log2Up(3)  // returns 2  log2Up(4)  // returns 2
    * }}}
    */
    object log2Ceil {
      def apply(x: BigInt): BigInt = {
          require(x > 0)
          bitLength(x - 1)
      }
    }  

`io.req.bits.fn`: 外部参数，等于4时表示`aluFn.FN_DIV`，此时`cmdMul := false`, `cmdHi := false`, `lhsSigned := true`, `rhsSigned := true`.
`req.dw`: 外部参数
`def halfWidth`: `w > 32`且`req.dw == false`的时候为`true`

### 只考虑unsign的情况时

#### w <= 32时

`def halfWidth`总返回`false`
`assume(io.req.bits.fn != 4)` => `lhsSigned == rhsSigned == false.B`
`def sext(x, halfW, signed)`总返回`x(w - 1, 0)`

- `val (lhs_in, lhs_sign) == (io.req.bits.in1(w - 1, 0), false)`
- `val (rhs_in, rhs_sign) == (io.req.bits.in2(w - 1, 0), false)`

`remainder == lhs_in == in1(w - 1, 0)`
`divisor == Cat(rhs_sign, rhs_in) == Cat(0, in2(w - 1, 0))`
`resHi == false.B` 
 => `result == remainder(w - 1, 0)`

除法中由于`fastMulW`等于`false`，因此`count`在`io.req.fire`状态中初始化为`0`

`cmdHi`总为`false`，因此`neg_out`等于`lhs_sign =/= rhs_sign` (只有异号的时候为`true`)

`outMul`在除法中总为`false`
`loOut`在除法中为`result(w / 2 - 1, 0)`
`hiOut`在`w <= 32`的除法中为`result(w - 1, w / 2)`
`io.resp.bits.data ：= Cat(hiOut, loOut)`，等于`result(w - 1, 0)`

### 关于result

remainder初始化为in1, 不管是eOut还是没有eOut，第一步必然得到一个0，即remainder第一次更新总是向左移动一位，最终当更新`w + 1`次时结束，最终的remainder第`w`位必然为`0`，低`w`位为结果（商）, 取`ghost_R`时，最后的`post-condition`为`ghost_R_next == remainder_next / Pow2(w + 1)`, `ghost_Q_next == remainder_next mod Pow2(w)`.

![rocket-div](../pic/rocket-div-manul.jpeg)

### 1208

突然发现不需要引入`ghost_R`了... 少写了`ghost_R`的更新和`ghost_R`跟`remainder`的关系，只需要`ghost_Q`，每次证明：
$\text{r} = 2^{i} * a - 2^{w + 1} * b * Q_{i} + Q_{i} \Rightarrow \\
 \text{r'} = 2^{i'} * a - 2^{w + 1} * b * Q_{i'} + Q_{i'}$ where $i' = i + 1$.
$i = w + 1$时结束计算，此时$\text{r} = 2^{w + 1} * (a - b * Q_{w + 1}) + Q_{w + 1}$.
