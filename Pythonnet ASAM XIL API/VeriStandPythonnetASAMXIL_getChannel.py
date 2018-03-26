import clr
import sys
import System

import os
import winreg
import time

sys.path.append("C:\\Windows\\Microsoft.NET\\assembly\\GAC_MSIL\\ASAM.XIL.Interfaces\\v4.0_2.0.1.0__bf471dff114ae984")

sys.path.append("c:\\Windows\\Microsoft.NET\\assembly\\GAC_MSIL\\ASAM.XIL.Implementation.Testbench\\v4.0_2.0.1.0__a258c402a414cddb")
sys.path.append("C:\\Windows\\Microsoft.NET\\assembly\\GAC_MSIL\\ASAM.XIL.Implementation.Framework\\v4.0_2.0.1.0__223668b9b1d3f17b")
sys.path.append("C:\\Windows\\Microsoft.NET\\assembly\\GAC_MSIL\\ASAM.XIL.Implementation.XILSupportLibrary\\v4.0_2.0.1.0__eb08b67b2f57b9b0")
sys.path.append("C:\\Windows\\Microsoft.NET\\assembly\\GAC_MSIL\\ASAM.XIL.Implementation.ManifestReader\\v4.0_2.0.1.0__8389d4d3a9402de1")
sys.path.append("C:\\Windows\\Microsoft.NET\\assembly\\GAC_MSIL\\ASAM.XIL.Implementation.Testbench\\v4.0_2.0.1.0__a258c402a414cddb")
sys.path.append("C:\\Windows\\Microsoft.NET\\assembly\\GAC_MSIL\\ASAM.XIL.Implementation.TestbenchFactory\\v4.0_2.0.1.0__fc9d65855b27d387")

clr.AddReference("ASAM.XIL.Interfaces")

import ASAM.XIL
from ASAM.XIL.Implementation.TestbenchFactory.Testbench import TestbenchFactory

tbFactory = TestbenchFactory()
print(tbFactory)

tb = tbFactory.CreateVendorSpecificTestbench("National Instruments", "NI VeriStand 2017 ASAM XIL Interface", "17.0.0")
print(tb)

maportFactory = ASAM.XIL.Interfaces.Testbench.MAPort.IMAPortFactory(tb.MAPortFactory)
print(maportFactory)

MyMAPort = maportFactory.CreateMAPort("NI MAPort 1")
print(MyMAPort)

config = MyMAPort.LoadConfiguration("c:\\Users\\Public\\Documents\\National Instruments\\NI VeriStand 2017\\Examples\\Stimulus Profile\\Engine Demo\\MAPortConfig.xml")
print(config)

MyMAPort.Configure(config, 1)
MyMAPort.StartSimulation()

time.sleep(3)

valueFact = tb.ValueFactory
writeVal = valueFact.CreateFloatValue(1000)

print('Reading Value:')
ReadVal = MyMAPort.Read("Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/b11")
retFloatVal = ReadVal
print(retFloatVal.Value)


print('Writing Value:')
print(writeVal.Value)

MyMAPort.Write("Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/b11", writeVal)
time.sleep(1)
NewReadVal = MyMAPort.Read("Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/b11")
print('Reading Value:')
print(NewReadVal.Value)

print('Sleep 15s')
time.sleep(15)

print('Closing')
MyMAPort.Disconnect()
MyMAPort.Dispose()

