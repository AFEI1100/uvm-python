#//
#// -------------------------------------------------------------
#//    Copyright 2004-2011 Synopsys, Inc.
#//    Copyright 2010 Mentor Graphics Corporation
#//    Copyright 2019-2020 Tuomas Poikela (tpoikela)
#//    All Rights Reserved Worldwide
#//
#//    Licensed under the Apache License, Version 2.0 (the
#//    "License"); you may not use self file except in
#//    compliance with the License.  You may obtain a copy of
#//    the License at
#//
#//        http://www.apache.org/licenses/LICENSE-2.0
#//
#//    Unless required by applicable law or agreed to in
#//    writing, software distributed under the License is
#//    distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#//    CONDITIONS OF ANY KIND, either express or implied.  See
#//    the License for the specific language governing
#//    permissions and limitations under the License.
#// -------------------------------------------------------------
#//

import cocotb
from cocotb.triggers import *

from uvm.seq.uvm_sequence import *
from uvm.macros import *
from uvm.base.uvm_config_db import UVMConfigDb
from uvm import run_test

from apb.apb_if import apb_if
from blk_env import blk_env
from blk_testlib import *


class dut_reset_seq(UVMSequence):

    def __init__(self, name="dut_reset_seq"):
        super().__init__(name)
        self.dut = None


    @cocotb.coroutine
    def body(self):
        self.dut.rst <= 1
        for i in range(5):
            yield FallingEdge(self.dut.clk)
        self.dut.rst <= 0

uvm_object_utils(dut_reset_seq)


@cocotb.test()
def initial(dut):
    env = blk_env("env")
    vif = apb_if(dut)
    UVMConfigDb.set(env, "apb", "vif", vif)
    yield run_test()