import magma as m
import mantle
import fault


class TFF(m.Circuit):
    IO = ["O", m.Out(m.Bit), "CLK", m.In(m.Clock)]

    @classmethod
    def definition(io):
        reg = mantle.Register(None, name="tff_reg")
        reg.CLK <= io.CLK
        reg.I <= ~reg.O
        io.O <= reg.O


tff_tester = fault.Tester(TFF, clock=TFF.CLK)
for i in range(8):
    tff_tester.circuit.O.expect(i % 2)
    tff_tester.step(2)
tff_tester.compile_and_run("verilator")
