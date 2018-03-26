import clr
import sys
import System

'''Run C:\\Users\\Public\\Documents\\National Instruments\\NI VeriStand 2017\\Examples\\Stimulus Profile\\Engine Demo\\Engine Demo.nivsproj'''

sys.path.append("c:\\Program Files (x86)\\National Instruments\\VeriStand 2017\\nivs.lib\\Reference Assemblies")
clr.AddReference("NationalInstruments.VeriStand.ClientAPI")
clr.AddReference("NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi")

from NationalInstruments.VeriStand.StimulusProfileDefinitionApi import StimulusProfile
from NationalInstruments.VeriStand.ClientAPI import Factory

#Instance of Class Factory provides access to the NI VeriStand system 
fac = Factory()
print(fac)

#Interface to perform basic workspace operations
facWork = fac.GetIWorkspace2('localhost')
print(facWork)

#Create StimulusProfile object and execute profile asynchronously. 
stimProfile = StimulusProfile("c:\\Users\\Public\\Documents\\National Instruments\\NI VeriStand 2017\\Examples\\Stimulus Profile\\Engine Demo\\Stimulus Profiles\\Basic Engine Demo\\Engine Demo Basics.nivsstimprof")
stimProfile.ExecuteAsync('localhost','000')

#define in out parameters
chan = System.String("Targets/Controller/Simulation Models/Models/Engine Demo/Outports/RPM")
out = System.Double(0)

error, out = facWork.GetSingleChannelValue(chan, out)
print("")
print("Error code:")
print(error.get_Code())
print("Channel name:")
print(chan)
print("Channel Value:")
print(out)

