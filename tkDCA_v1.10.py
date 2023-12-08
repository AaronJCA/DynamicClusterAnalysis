from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
from pylab import figure, show
import matplotlib.pyplot as plt
import tkinter
import numpy
import math
from tkinter import ttk
from tkinter import filedialog
import csv
import copy
import string

iconData = '''R0lGODlhEAAQAPcAAAAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr/wBVAABVMwBV
        ZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCqmQCqzACq/wDVAADVMwDVZgDV
        mQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMr
        zDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq
        /zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2Yr
        AGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA/2aqAGaq
        M2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/mWb/zGb//5kAAJkAM5kA
        ZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplVmZlVzJlV/5mAAJmAM5mAZpmA
        mZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/
        zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV
        /8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV/8z/
        AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8rmf8rzP8r//9VAP9V
        M/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+qzP+q///VAP/VM//V
        Zv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAAACH5BAEAAPwALAAAAAAQABAA
        AAiKADt04CCQ4MCCCAlaOLiQwwWCDiEyHMihYoeHBzs0pFiRA4CCDy0OvFAQgEmKAjUe9Ghyn0mL
        EgWaBLCv5kuFHlm2rOkSAByCM2n25NnzQsudQ3kGrRlDaFKbAAwEnUq1alUiGjRkyDBEA5GvQ4Zk
        wOr169YPRJSYFUsEBIivH5KETfI1idywXwMCADs=
        '''

ionChoices1 = []
ionChoices1 = [
    'NA'
]

sampleChoices = []
sampleChoices = [
    'NA'
]

polarityChoices = []
polarityChoices = [
    'Positive',
    'Negative'
]

modeChoices1 = []
modeChoices1 = [
    'DCA-Hal',
    'DCA-Sul',
    #'DCA-Bor', #For compounds containing boron
    'All Features'
]

featureChoices1 = []
featureChoices1 = [
    'Chemical',
    'Molecular'
]

class simpleapp_tk(tkinter.Tk):
    def __init__(primary,parent):
        tkinter.Tk.__init__(primary,parent)
        primary.parent = parent
        primary.initialize()
        primary.update()
        primary.minsize(primary.winfo_width(), primary.winfo_height())

    def initialize(primary):
        primary.grid()
        primary.grid_rowconfigure(25,weight=1)
        primary.grid_columnconfigure(10,weight=1)

        primary.massList = []
        primary.abundanceList = []
        primary.masterList = []
        
        primary.rtVar = StringVar()
        primary.mzVar = StringVar()
        primary.areaVar = StringVar()
        primary.requireVar = StringVar()
        primary.sepVar = StringVar()
        primary.rawMasterList = []
        primary.rawMZCol = IntVar()
        primary.rawRTCol = IntVar()
        primary.resultsMasterList = []
        primary.resultsMasterRateList = []
        primary.filterMode = ""
        primary.currentFileName = ""
        primary.selectedSep = StringVar()
        primary.selectedSample = StringVar()
        primary.selectedFeature = StringVar()
        primary.radioSelect = StringVar()
        primary.rSel = StringVar()
        primary.selectedMode = StringVar()
        primary.selectedPolarity = StringVar()
        primary.minRTVar = StringVar()
        primary.minIIVar = StringVar()
        primary.rTConvertionUnit = 0
        
        color = '0.9'

        plotFrame = Frame(primary, width=654, height=500)
        plotFrame.grid_propagate(False)
        plotFrame.grid_rowconfigure(25, weight=1)
        plotFrame.grid_columnconfigure(10, weight=1)
        plotFrame.grid(row=2, column=10, columnspan=2, rowspan=25, sticky="neswn")
 
        fig = Figure()
        rect = fig.patch
        rect.set_facecolor(color)

        primary.canvas = FigureCanvasTkAgg(fig, plotFrame)
        primary.canvas.get_tk_widget().grid(row=2, column=10, columnspan=2, rowspan=25, sticky="neswn")

        toolbar_frame = Frame(primary)
        toolbar_frame.grid(row = 1, column = 10, sticky=W)
        toolbar = NavigationToolbar2Tk(primary.canvas, toolbar_frame)
        toolbar.grid(row=1, column=10, columnspan=5, sticky=W)
        toolbar.update()
        
        primary.ax2 = fig.add_subplot(1,1,1)
        primary.ax2.set_xlabel('Mass to charge (m/z)')
        primary.ax2.set_title('Isotope Pattern')
        primary.ax2.set_ylabel('Relative Abundance')
        primary.canvas.draw()

        primary.CSVBtn = Button(primary, text='Import CSV', command=primary.getFileName)
        primary.CSVBtn.grid(row=1, column=1, columnspan=5, pady=(10,10))

        primary.sampleLabel = Label(primary, text="Current sample:")
        primary.sampleLabel.grid(row=2, column=1, sticky=E)
        primary.sampleOptions = ttk.Combobox(primary, state='readonly', width=15, textvariable=primary.selectedSample)
        primary.sampleOptions["values"] = sampleChoices
        primary.sampleOptions.set("NA")
        primary.sampleOptions.grid(row=2, column=2, columnspan=4, sticky=SW)

        primary.rtVarLabel = Label(primary, text="RT drift:")
        primary.rtVarLabel.grid(row=3, column=1, sticky=E) 
        primary.rtVarVal = Entry(primary, textvariable=primary.rtVar, width=15)
        primary.rtVarVal.grid(row=3, column=2, sticky=W)
        primary.rtVarVal.insert(0, 1.0)
        primary.rtVarValMinLabel = Label(primary, text="± sec")
        primary.rtVarValMinLabel.grid(row=3, column=3, sticky=W)

        primary.mzVarLabel = Label(primary, text="Mass error:")
        primary.mzVarLabel.grid(row=4, column=1, sticky=E) 
        primary.mzVarVal = Entry(primary, textvariable=primary.mzVar, width=15)
        primary.mzVarVal.grid(row=4, column=2, sticky=W)
        primary.mzVarVal.insert(0, 5)
        primary.mzVarValDaLabel = Label(primary, text="ppm")
        primary.mzVarValDaLabel.grid(row=4, column=3, sticky=W)

        primary.modeLabel = Label(primary, text="Detector polarity:")
        primary.modeLabel.grid(row=5, column=1, sticky=E)
        primary.modeOptions = ttk.Combobox(primary, state='readonly', width=15, textvariable=primary.selectedPolarity)
        primary.modeOptions["values"] = polarityChoices
        primary.modeOptions.set("Positive")
        primary.modeOptions.grid(row=5, column=2, columnspan=4, sticky=SW)

##        primary.minIIVarLabel = Label(primary, text="Min. Isotope Area:")
##        primary.minIIVarLabel.grid(row=6, column=1, sticky=E) 
##        primary.minIIVarVal = Entry(primary, textvariable=primary.minIIVar, width=15)
##        primary.minIIVarVal.grid(row=6, column=2, sticky=W)
##        primary.minIIVarVal.insert(0, 0)

        primary.findBtn = Button(primary, text='Find Features', command=primary.findIsoAndComps)
        primary.findBtn.grid(row=7, column=1, columnspan=5, pady=(10,10))

        primary.modeLabel = Label(primary, text="Filter:")
        primary.modeLabel.grid(row=8, column=1, sticky=E)
        primary.modeOptions = ttk.Combobox(primary, state='readonly', width=15, textvariable=primary.selectedMode)
        primary.modeOptions["values"] = modeChoices1
        primary.modeOptions.set("DCA-Hal")
        primary.modeOptions.grid(row=8, column=2, columnspan=4, sticky=SW)

        primary.areaVarLabel = Label(primary, text="Area cut-off:")
        primary.areaVarLabel.grid(row=9, column=1, sticky=E) 
        primary.areaVarVal = Entry(primary, textvariable=primary.areaVar, width=15)
        primary.areaVarVal.grid(row=9, column=2, sticky=W)
        primary.areaVarVal.insert(0, 100)

        primary.requireVarLabel = Label(primary, text="Required Rate:")
        primary.requireVarLabel.grid(row=11, column=1, sticky=E) 
        primary.requireVarVal = Entry(primary, textvariable=primary.requireVar, width=15)
        primary.requireVarVal.grid(row=11, column=2, sticky=W)
        primary.requireVarVal.insert(0, 50)
        primary.requireVarValLabel = Label(primary, text="%")
        primary.requireVarValLabel.grid(row=11, column=3, sticky=W)

        primary.featureVarLabel = Label(primary, text="Feature mode:")
        primary.featureVarLabel.grid(row=10, column=1, sticky=E)
        primary.selectedFeature.trace('w', primary.FeatureRefresh) 
        primary.featureOptions = ttk.Combobox(primary, state='readonly', width=15, textvariable=primary.selectedFeature)
        primary.featureOptions["values"] = featureChoices1
        primary.featureOptions.set("Chemical")
        primary.featureOptions.grid(row=10, column=2, columnspan=4, sticky=SW)
        
        primary.filterBtn = Button(primary, text='Apply Filter', command=primary.applyFilter)
        primary.filterBtn.grid(row=12, column=1, columnspan=5, pady=(10,0))

        primary.sepLabel = Label(primary, text="Filtered Features:")
        primary.sepLabel.grid(row=13, column=1, pady=(5,0), sticky=E)
        primary.sepOptions = ttk.Combobox(primary, state='readonly', width=22, textvariable=primary.selectedSep)
        primary.sepOptions["values"] = ionChoices1
        primary.sepOptions.set("NA")
        primary.sepOptions.grid(row=13, column=2, columnspan=4, pady=(10,0), sticky=SW)
        primary.sepOptions.bind("<<ComboboxSelected>>", primary.grph)

        primary.txt = Text(primary, borderwidth=3, relief="sunken")
        primary.txt.config(font=("consolas", 9), undo=True, wrap='word', width=35, height=20)
        primary.txt.grid(row=20, column=1, columnspan=4, rowspan=3, sticky=E, padx=2, pady=5)
        primary.txt.configure(state="disabled")
        scrollb = Scrollbar(primary, command=primary.txt.yview)
        scrollb.grid(row=20, column=6, rowspan=3, sticky=W+N+S, padx=(0,20), pady=5)
        primary.txt['yscrollcommand'] = scrollb.set

        primary.CSVExportBtn = Button(primary, text='Export Results', command=primary.exportAsCSV)
        primary.CSVExportBtn.grid(row=23, column=1, columnspan=5, pady=(10,10))

    def FeatureRefresh(primary, *args):
        
        featureMode = primary.selectedFeature.get()
        
        if featureMode == "Molecular":
            result = primary.requireVarVal.configure(state="normal")
            
        if featureMode == "Chemical":
            result = primary.requireVarVal.configure(state="disabled")

        return

    def getFileName(primary):
        fileName = filedialog.askopenfilename(filetypes=[('csv (Comma delimited)', '*.csv')])
        justTheFile = StringVar

        def isfloat(value):
          try:
            float(value)
            return True
          except ValueError:
            return False

        if fileName != "":
            justTheFile = fileName.split('/')
            justTheFile = justTheFile[len(justTheFile)-1]
            app.title('DCAnalysis 1.10 - ' + justTheFile)
            primary.currentFileName = justTheFile
            
            csvRaw = csv.reader(open(fileName, 'U'), dialect='excel')

            ionIDList = []
            mzList = []
            RTList = []
            peakAList = []
            completeList = []
            rTMin = 0
            rTMax = 0
            rTAv = 0
            rTSum = 0

            sampleList = list(csvRaw)

            for row in csvRaw:
                numCols = 0
                for col in row:
                    numCols = numCols + 1

            listLen = 0
            maxRT = 0
            mzCol = 0
            RTCol = 0
            n = 0
            sampleCol = []
            n1 = 0

            while n < len(sampleList[0]):
                if "mz" in sampleList[0][n] or "m/z" in sampleList[0][n] or "MZ" in sampleList[0][n] or "M/Z" in sampleList[0][n]:
                    if mzCol == 0:
                        mzCol = n
                if "rt" in sampleList[0][n] or "RT" in sampleList[0][n] or "Rt" in sampleList[0][n]:
                    if RTCol == 0:
                        RTCol = n
                n = n + 1

            colTotal = 0
            colNumber = 0
            cOS = 1
            rOS = 1
            
            while cOS < len(sampleList[0]):
                colNumber = cOS
                while rOS < len(sampleList):
                    if isfloat(sampleList[rOS][cOS]) == True:
                        if float(sampleList[rOS][cOS]) == float('Inf'):
                            colTotal = colTotal + 0
                        else:
                            colTotal = colTotal + float(sampleList[rOS][cOS])
                        
                    rOS = rOS + 1

                if colTotal / rOS > 2000:
                    sampleCol.append(colNumber)
                rOS = 1
                colTotal = 0
                cOS = cOS + 1

            sampleColNames = []
            cOS = 0

            while cOS < len(sampleCol):
                sampleColNames.append(sampleList[0][sampleCol[cOS]])
                cOS = cOS + 1

            sampleChoices = sampleColNames
            primary.sampleOptions.set(sampleChoices[0])
            primary.sampleOptions["values"] = sampleChoices     

            primary.rawMZCol = mzCol
            primary.rawRTCol = RTCol
            primary.rawMasterList = sampleList
 
            primary.txt.configure(state="normal")
            primary.txt.delete(1.0, END)
            primary.txt.insert('1.0', "File loaded" + '\n')
            primary.txt.configure(state="disabled")

        return
    
    #Sorts isotopomers into chemical features 
    def findIsoAndComps(primary):

        if primary.selectedSample.get() == "NA":
            return

        RTChange = DoubleVar
        MZChange = DoubleVar
        areaCutOff = DoubleVar
        SepToFind = DoubleVar
        currentRT = DoubleVar
        currentMZ = DoubleVar
        currentAbd = DoubleVar
        testStr = StringVar
        halogenDevMax = DoubleVar
        halogenDevMin = DoubleVar
        halogenDevMax = 1.00584801
        halogenDevMin = 0.99080011
        maxRT = 0
        mzCol = IntVar
        RTCol = IntVar
        paCol = IntVar
        mzCol = primary.rawMZCol
        rtCol = primary.rawRTCol
        paCol = 0
        
        rawList = []
        firstList = []
        firstList = copy.deepcopy(primary.rawMasterList)

        currentSample = primary.selectedSample.get()

        n = 0
        while firstList[0][n] != currentSample:
            n = n + 1
        paCol = n

        n = 1
        while n < len(firstList):
            if float(firstList[n][rtCol]) > float(maxRT):
                maxRT = float(firstList[n][rtCol])
            n = n + 1

        if float(maxRT) < 150:
            primary.rTConvertionUnit = 60
        else:
            primary.rTConvertionUnit = 1
        #firstList[1:][rtCol] = firstList[1:][rtCol] * primary.rTConvertionUnit

        n = 1
        while n < len(firstList):
            rawList.append([float(firstList[n][0]), float(firstList[n][mzCol]), float('%.1f' % (float(firstList[n][rtCol])*primary.rTConvertionUnit)), float(firstList[n][paCol]), 0, 0, ""])
            n = n + 1

        rawList = sorted(rawList,key=lambda l:l[1], reverse=False) #Sorted by [1] MZ (RT = 2, ID = 0, PA = 3)

        editedList = []
        n = 0
        n1 = 1
        targetIonList = []
        targetIon = 0
        ppmError = float(primary.mzVar.get())
        RTChange = float(primary.rtVar.get())
        minRT = 0

        #This loop matches isotopomers on RT which are within a Da window for triply, double and singly charge ions.
        while n < len(rawList):
            if float(rawList[n][2]) > (minRT*60) and float(rawList[n][3]) > 0: #rawList[n][3] is the minimum area
                currentMZ = float(rawList[n][1])
                currentRT = float(rawList[n][2])
                currentAbd = float(rawList[n][3])
                MZChange = currentMZ / 1000000 * ppmError / 2

                while n1 < len(rawList):
                    if float(rawList[n1][2]) < (currentRT + RTChange):
                        
                        if float(rawList[n1][2]) > (currentRT - RTChange):

                            if rawList[n][5] == 0:

                                #Triply charged features  
                                if ((float(rawList[n1][1]) < ((currentMZ + (halogenDevMax / 3)) + MZChange) and \
                                    float(rawList[n1][1]) > ((currentMZ + (halogenDevMin / 3)) - MZChange)) or \
                                    (float(rawList[n1][1]) < ((currentMZ - (halogenDevMax / 3)) + MZChange) and \
                                    float(rawList[n1][1]) > ((currentMZ - (halogenDevMin / 3)) - MZChange))):

                                    if float(rawList[n1][3]) / currentAbd < 6 and float(rawList[n1][3]) / currentAbd > 0.0000082*currentMZ**1.1098:
                                        rawList[n][4] = 3
                                        rawList[n][5] = rawList[n1][0]
                                        
                                #Doubly charged features 
                                elif ((float(rawList[n1][1]) < ((currentMZ + (halogenDevMax / 2)) + MZChange) and \
                                    float(rawList[n1][1]) > ((currentMZ + (halogenDevMin / 2)) - MZChange)) or \
                                    (float(rawList[n1][1]) < ((currentMZ - (halogenDevMax / 2)) + MZChange) and \
                                    float(rawList[n1][1]) > ((currentMZ - (halogenDevMin / 2)) - MZChange))):

                                    if float(rawList[n1][3]) / currentAbd < 6 and float(rawList[n1][3]) / currentAbd >  0.0000082*currentMZ**1.1098: 
                                        rawList[n][4] = 2
                                        rawList[n][5] = rawList[n1][0]

                                #Singly charged features
                                elif ((float(rawList[n1][1]) < ((currentMZ + halogenDevMax) + MZChange) and \
                                    float(rawList[n1][1]) > ((currentMZ + halogenDevMin) - MZChange)) or \
                                    (float(rawList[n1][1]) < ((currentMZ - halogenDevMax) + MZChange) and \
                                    float(rawList[n1][1]) > ((currentMZ - halogenDevMin) - MZChange))):

                                    if float(rawList[n1][3]) / currentAbd < 6 and float(rawList[n1][3]) / currentAbd > 0.0000082*currentMZ**1.1098:
                                        rawList[n][4] = 1
                                        rawList[n][5] = rawList[n1][0]

                                        #print (rawList[n1])
                                        #print ("Found: " + str(currentMZ) + " _ " + str(rawList[n1][1]))

                    n1 = n1 + 1

            n = n + 1
            n1 = n + 1

        n = n - 1
        n1 = 0
        counter = 0
        editedList = rawList[:][:]
        
        while n != -1:
            if editedList[n][5] != 0:

                targetIon = editedList[n][5]
                counter = counter + 1

                while float(editedList[n1][0]) != float(targetIon):
                    n1 = n1 + 1

                #Chance charge state to the most charged
                if float(editedList[n][4]) < float(editedList[n1][4]):
                    editedList[n][4] = editedList[n1][4]

                if editedList[n1][5] == 0:
                    editedList[n][5] =  str(editedList[n1][1]) + "-" + str(editedList[n1][2]) + "-" + str(editedList[n1][3]) + ":" 
                else:
                    editedList[n][5] = str(editedList[n1][1]) + "-" + str(editedList[n1][2]) + "-" + str(editedList[n1][3]) + ":" + str(editedList[n1][5])
                    
                editedList[n1][1] = "0"
                editedList[n1][2] = "0"
                editedList[n1][3] = "0"
                editedList[n1][4] = "0"
                editedList[n1][5] = 0
                
            n1 = 0
            n = n - 1

        counter = counter - 1
        filterList = []
        n = 1
        numberOfIsos = 0

        #Changes all features with 1 or less isotopomers to "0"
        while n < len(editedList):
            
            if editedList[n][5] != 0:
                numberOfIsos = editedList[n][5].count(':')
            
            if numberOfIsos < 2:
                editedList[n][1] = "0"
                editedList[n][2] = "0"
                editedList[n][3] = "0"
                editedList[n][4] = "0"
                editedList[n][5] = 0
                
            if editedList[n][5] == 0:
                editedList[n][1] = "0"
                editedList[n][2] = "0"
                editedList[n][3] = "0"
                editedList[n][4] = "0"
                editedList[n][5] = 0

            n = n + 1
            numberOfIsos = 50
                
        n = 0

        #Removes all features with 1 or less isotopomers
        while n < len(editedList):
            if editedList[n][1] != "0":
                filterList.append(editedList[n])
            n = n + 1

        #print(filterList)

        primary.masterList = filterList
        primary.compileMF()
        
        return

    #Compiles chemical features into molecular features
    def compileMF(primary):

        filterList = primary.masterList
        RTChange = float(primary.rtVar.get())
        ppmError = float(primary.mzVar.get())
        targetIonList = []
        currentIon = DoubleVar
        currentRT = DoubleVar
        MZChange = DoubleVar
        filterFind = 0
        mFNum = 1
        changeMFNum = 0
        detectorPolarity = primary.selectedPolarity.get()
        n = 0
        largerIonRow = 0
        smallerIonRow = 0
        hitDetect = 0
        n2 = 0
        
        while n < len(filterList):        
           filterList[n][0] = 0
           n = n + 1

        n = 0
        n1 = 0
        
        #Loop to search for the mass difference between a chemical feature and common adducts and fragments, K, Na, NH4, and -H2O etc.
        while n < len(filterList):

            mFNum = mFNum + 1

            if filterList[n][0] == 0 and filterList[n][4] != 0:
                currentIon = float(filterList[n][1]) * float(filterList[n][4])
                filterList[n][0] = mFNum
                
                MZChange = currentIon / 1000000 * ppmError
                currentRT = filterList[n][2]
            else:
                n1 = len(filterList)
            
            while n1 < len(filterList):
                if filterList[n][4] != 0:
                    compareIon = float(filterList[n1][1]) * float(filterList[n1][4])
                else:
                    compareIon = float(filterList[n1][1])
                
                if float(filterList[n1][2]) < (currentRT + RTChange) and \
                        float(filterList[n1][2]) > (currentRT - RTChange):

                    smallerIonRow = n
                    largerIonRow = n1
                    if float(currentIon) > float(compareIon):
                        largerIonRow = n
                        smallerIonRow = n1

                    if detectorPolarity == "Positive" and filterList[n1][4] == filterList[n][4]:

                        if float(compareIon) > (float(currentIon) + 4.95539) - MZChange and float(compareIon) < (float(currentIon) + 4.95539) + MZChange or \
                           float(currentIon) > (float(compareIon) + 4.95539) - MZChange and float(currentIon) < (float(compareIon) + 4.95539) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M+NH4]+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+Na]+"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M+NH4+" + str(filterList[smallerIonRow][4]) + "H]" + str(filterList[smallerIonRow][4]) + "+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+Na+" + str(filterList[largerIonRow][4]) + "H]" + str(filterList[largerIonRow][4]) + "+"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("Na-NH4 _ " + str(currentIon) + " _ " + str(compareIon))
                            #print (filterList[n1])
                            
                        elif float(compareIon) > (float(currentIon) + 15.97394) - MZChange and float(compareIon) < (float(currentIon) + 15.97394) + MZChange or \
                             float(currentIon) > (float(compareIon) + 15.97394) - MZChange and float(currentIon) < (float(compareIon) + 15.97394) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M+Na]+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+K]+"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M+Na+" + str(int(filterList[smallerIonRow][4])-1) + "H]" + str(filterList[smallerIonRow][4]) + "+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+K+" + str(int(filterList[largerIonRow][4])-1) + "H]" + str(filterList[largerIonRow][4]) + "+"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("K-Na _ " + str(currentIon) + " _ " + str(compareIon))
                            #print (filterList[n1])
                            
                        elif float(compareIon) > (float(currentIon) + 17.02655) - MZChange and float(compareIon) < (float(currentIon) + 17.02655) + MZChange or \
                           float(currentIon) > (float(compareIon) + 17.02655) - MZChange and float(currentIon) < (float(compareIon) + 17.02655) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M+H]+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+NH4]+"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M+" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+NH4+" + str(int(filterList[largerIonRow][4])-1) + "H]" + str(filterList[largerIonRow][4]) + "+"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("NH4-M _ " + str(currentIon) + " _ " + str(compareIon))
                            #print (filterList[n1])
                            
                        elif float(compareIon) > (float(currentIon) + 18.01057) - MZChange and float(compareIon) < (float(currentIon) + 18.01057) + MZChange or \
                           float(currentIon) > (float(compareIon) + 18.01057) - MZChange and float(currentIon) < (float(compareIon) + 18.01057) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H2O+H]+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+H]+"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H2O+" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+" + str(int(filterList[largerIonRow][4])) + "H]" + str(filterList[largerIonRow][4]) + "+"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("M-H2O _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]
                            
                        elif float(compareIon) > (float(currentIon) + 20.92933) - MZChange and float(compareIon) < (float(currentIon) + 20.92933) + MZChange or \
                           float(currentIon) > (float(compareIon) + 20.92933) - MZChange and float(currentIon) < (float(compareIon) + 20.92933) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M+NH4]+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+K]+"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M+NH4" + str(int(filterList[smallerIonRow][4])-1) + "H]" + str(filterList[smallerIonRow][4]) + "+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+K" + str(int(filterList[largerIonRow][4])-1) + "H]" + str(filterList[largerIonRow][4]) + "+"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("K-NH4 _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]
                            
                        elif float(compareIon) > (float(currentIon) + 21.98194) - MZChange and float(compareIon) < (float(currentIon) + 21.98194) + MZChange or \
                           float(currentIon) > (float(compareIon) + 21.98194) - MZChange and float(currentIon) < (float(compareIon) + 21.98194) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M+H]+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+Na]+"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M+" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+Na" + str(int(filterList[largerIonRow][4])-1) + "H]" + str(filterList[largerIonRow][4]) + "+"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("Na-M _ " + str(currentIon) + " _ " + str(compareIon))
   
                        elif float(compareIon) > (float(currentIon) + 35.03712) - MZChange and float(compareIon) < (float(currentIon) + 35.03712) + MZChange or \
                           float(currentIon) > (float(compareIon) + 35.03712) - MZChange and float(currentIon) < (float(compareIon) + 35.03712) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H2O+H]+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+NH4]+"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H2O+" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+NH4" + str(int(filterList[largerIonRow][4])-1) + "H]" + str(filterList[largerIonRow][4]) + "+"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("NH4-H2O _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]
                            
                        elif float(compareIon) > (float(currentIon) + 35.97668) - MZChange and float(compareIon) < (float(currentIon) + 35.97668) + MZChange or \
                           float(currentIon) > (float(compareIon) + 35.97668) - MZChange and float(currentIon) < (float(compareIon) + 35.97668) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-HCl+H]+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+H]+"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-HCl+" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+" + str(int(filterList[largerIonRow][4])) + "H]" + str(filterList[largerIonRow][4]) + "+"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("M-HCl _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]
                            
                        elif float(compareIon) > (float(currentIon) + 37.95588) - MZChange and float(compareIon) < (float(currentIon) + 37.95588) + MZChange or \
                           float(currentIon) > (float(compareIon) + 37.95588) - MZChange and float(currentIon) < (float(compareIon) + 37.95588) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M+H]+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+K]+"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M+" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+K+" + str(int(filterList[largerIonRow][4])-1) + "H]" + str(filterList[largerIonRow][4]) + "+"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("K-M _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        elif float(compareIon) > (float(currentIon) + 39.99251) - MZChange and float(compareIon) < (float(currentIon) + 39.99251) + MZChange or \
                           float(currentIon) > (float(compareIon) + 39.99251) - MZChange and float(currentIon) < (float(compareIon) + 39.99251) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H2O+H]+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+Na]+"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H2O+" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+Na+" + str(int(filterList[largerIonRow][4])-1) + "H]" + str(filterList[largerIonRow][4]) + "+"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("Na-H2O _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        elif float(compareIon) > (float(currentIon) + 55.96645) - MZChange and float(compareIon) < (float(currentIon) + 55.96645) + MZChange or \
                           float(currentIon) > (float(compareIon) + 55.96645) - MZChange and float(currentIon) < (float(compareIon) + 55.96645) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H2O+H]+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+K]+"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H2O+" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+K+" + str(int(filterList[largerIonRow][4])-1) + "H]" + str(filterList[largerIonRow][4]) + "+"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("K-H2O _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        elif float(compareIon) > (float(currentIon) + 79.92617) - MZChange and float(compareIon) < (float(currentIon) + 79.92617) + MZChange or \
                           float(currentIon) > (float(compareIon) + 79.92617) - MZChange and float(currentIon) < (float(compareIon) + 79.92617) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-HBr+H]+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+H]+"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-HBr+" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+" + str(int(filterList[largerIonRow][4])) + "H]" + str(filterList[largerIonRow][4]) + "+"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("M-HBr _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        elif float(compareIon) > (float(currentIon) + 79.95682) - MZChange and float(compareIon) < (float(currentIon) + 79.95682) + MZChange or \
                           float(currentIon) > (float(compareIon) + 79.95682) - MZChange and float(currentIon) < (float(compareIon) + 79.95682) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-SO3+H]+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+H]+"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-SO3+" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "+"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+" + str(int(filterList[largerIonRow][4])) + "H]" + str(filterList[largerIonRow][4]) + "+"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("M-SO3 _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        #elif float(compareIon) > (float(currentIon) + 17.96611) - MZChange and float(compareIon) < (float(currentIon) + 17.96611) + MZChange or \
                        #   float(currentIon) > (float(compareIon) + 17.96611) - MZChange and float(currentIon) < (float(compareIon) + 17.96611) + MZChange:
                        #    filterList[n1][0] = mFNum
                            #print ("H2O-HCl _ " + str(currentIon) + " _ " + str(compareIon))
                            #print (filterList[n1])

                        #elif float(compareIon) > (float(currentIon) + 53.00323) - MZChange and float(compareIon) < (float(currentIon) + 53.00323) + MZChange or \
                        #   float(currentIon) > (float(compareIon) + 53.00323) - MZChange and float(currentIon) < (float(compareIon) + 53.00323) + MZChange:
                        #    filterList[n1][0] = mFNum
                            #print ("NH4-HCl _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        #elif float(compareIon) > (float(currentIon) + 57.95862) - MZChange and float(compareIon) < (float(currentIon) + 57.95862) + MZChange or \
                        #   float(currentIon) > (float(compareIon) + 57.95862) - MZChange and float(currentIon) < (float(compareIon) + 57.95862) + MZChange:
                        #    filterList[n1][0] = mFNum
                            #print ("Na-HCl _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        #elif float(compareIon) > (float(currentIon) + 61.9156) - MZChange and float(compareIon) < (float(currentIon) + 61.9156) + MZChange or \
                        #   float(currentIon) > (float(compareIon) + 61.9156) - MZChange and float(currentIon) < (float(compareIon) + 61.9156) + MZChange:
                        #    filterList[n1][0] = mFNum
                            #print ("H2O-HBr _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        #elif float(compareIon) > (float(currentIon) + 61.94625) - MZChange and float(compareIon) < (float(currentIon) + 61.94625) + MZChange or \
                        #   float(currentIon) > (float(compareIon) + 61.94625) - MZChange and float(currentIon) < (float(compareIon) + 61.94625) + MZChange:
                        #    filterList[n1][0] = mFNum
                            #print ("H2O-SO3 _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        #elif float(compareIon) > (float(currentIon) + 73.93256) - MZChange and float(compareIon) < (float(currentIon) + 73.93256) + MZChange or \
                        #   float(currentIon) > (float(compareIon) + 73.93256) - MZChange and float(currentIon) < (float(compareIon) + 73.93256) + MZChange:
                        #    filterList[n1][0] = mFNum
                            #print ("K-HCl _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        #elif float(compareIon) > (float(currentIon) + 96.95272) - MZChange and float(compareIon) < (float(currentIon) + 96.95272) + MZChange or \
                        #   float(currentIon) > (float(compareIon) + 96.95272) - MZChange and float(currentIon) < (float(compareIon) + 96.95272) + MZChange:
                        #    filterList[n1][0] = mFNum
                            #print ("NH4-HBr _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        #elif float(compareIon) > (float(currentIon) + 96.98337) - MZChange and float(compareIon) < (float(currentIon) + 96.98337) + MZChange or \
                        #   float(currentIon) > (float(compareIon) + 96.98337) - MZChange and float(currentIon) < (float(compareIon) + 96.98337) + MZChange:
                        #    filterList[n1][0] = mFNum
                            #print ("NH4-SO3 _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        #elif float(compareIon) > (float(currentIon) + 101.90811) - MZChange and float(compareIon) < (float(currentIon) + 101.90811) + MZChange or \
                        #   float(currentIon) > (float(compareIon) + 101.90811) - MZChange and float(currentIon) < (float(compareIon) + 101.90811) + MZChange:
                        #    filterList[n1][0] = mFNum
                            #print ("Na-HBr _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        #elif float(compareIon) > (float(currentIon) + 101.93876) - MZChange and float(compareIon) < (float(currentIon) + 101.93876) + MZChange or \
                        #   float(currentIon) > (float(compareIon) + 101.93876) - MZChange and float(currentIon) < (float(compareIon) + 101.93876) + MZChange:
                        #    filterList[n1][0] = mFNum
                            #print ("Na-SO3 _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        #elif float(compareIon) > (float(currentIon) + 117.88205) - MZChange and float(compareIon) < (float(currentIon) + 117.88205) + MZChange or \
                        #   float(currentIon) > (float(compareIon) + 117.88205) - MZChange and float(currentIon) < (float(compareIon) + 117.88205) + MZChange:
                        #    filterList[n1][0] = mFNum
                            #print ("K-HBr _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        #elif float(compareIon) > (float(currentIon) + 117.9127) - MZChange and float(compareIon) < (float(currentIon) + 117.9127) + MZChange or \
                        #   float(currentIon) > (float(compareIon) + 117.9127) - MZChange and float(currentIon) < (float(compareIon) + 117.9127) + MZChange:
                        #    filterList[n1][0] = mFNum
                            #print ("K-SO3 _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                    elif  filterList[n1][4] == filterList[n][4]:
                        if float(compareIon) > (float(currentIon) + 18.01057) - MZChange and float(compareIon) < (float(currentIon) + 18.01057) + MZChange or \
                           float(currentIon) > (float(compareIon) + 18.01057) - MZChange and float(currentIon) < (float(compareIon) + 18.01057) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H2O-H]-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M-H]-"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H2O-" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M-" + str(int(filterList[largerIonRow][4])) + "H]" + str(filterList[largerIonRow][4]) + "-"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("[M-H2O-H] _ " + str(currentIon) + " _ " + str(compareIon))
                            #print (filterList[n1])
                            
                        elif float(compareIon) > (float(currentIon) + 21.981939) - MZChange and float(compareIon) < (float(currentIon) + 21.981939) + MZChange or \
                             float(currentIon) > (float(compareIon) + 21.981939) - MZChange and float(currentIon) < (float(compareIon) + 21.981939) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H]-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+Na-2H]-"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+Na-" + str(int(filterList[largerIonRow][4])+1) + "H]" + str(filterList[largerIonRow][4]) + "-"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("[M-Na-2H] _ " + str(currentIon) + " _ " + str(compareIon))
                            #print (filterList[n1])
                            
                        elif float(compareIon) > (float(currentIon) + 35.97667) - MZChange and float(compareIon) < (float(currentIon) + 35.97667) + MZChange or \
                           float(currentIon) > (float(compareIon) + 35.97667) - MZChange and float(currentIon) < (float(compareIon) + 35.97667) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H]-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+Cl]-"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+Cl-" + str(int(filterList[largerIonRow][4])-1) + "H]" + str(filterList[largerIonRow][4]) + "-"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("[M+Cl] _ " + str(currentIon) + " _ " + str(compareIon))
                            #print (filterList[n1])
                            
                        elif float(compareIon) > (float(currentIon) + 60.02112) - MZChange and float(compareIon) < (float(currentIon) + 60.02112) + MZChange or \
                           float(currentIon) > (float(compareIon) + 60.02112) - MZChange and float(currentIon) < (float(compareIon) + 60.02112) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H]-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+CH3COOH-H]-"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+CH3COOH-" + str(int(filterList[largerIonRow][4])) + "H]" + str(filterList[largerIonRow][4]) + "-"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("[M+FA-H] _ " + str(currentIon) + " _ " + str(compareIon))
                            #print (filterList[n1])

                        elif float(compareIon) > (float(currentIon) + 46.00547) - MZChange and float(compareIon) < (float(currentIon) + 46.00547) + MZChange or \
                           float(currentIon) > (float(compareIon) + 46.00547) - MZChange and float(currentIon) < (float(compareIon) + 46.00547) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H]-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+CHOOH-H]-"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+CHOOH-" + str(int(filterList[largerIonRow][4])) + "H]" + str(filterList[largerIonRow][4]) + "-"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("[M+FA-H] _ " + str(currentIon) + " _ " + str(compareIon))
                            #print (filterList[n1])
                            
                        elif float(compareIon) > (float(currentIon) + 17.02655) - MZChange and float(compareIon) < (float(currentIon) + 17.02655) + MZChange or \
                           float(currentIon) > (float(compareIon) + 17.02655) - MZChange and float(currentIon) < (float(compareIon) + 17.02655) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-H]-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+NH4-2H]-"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M+NH4-" + str(int(filterList[largerIonRow][4])+1) + "H]" + str(filterList[largerIonRow][4]) + "-"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("[M+NH4-H] _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]

                        elif float(compareIon) > (float(currentIon) + 27.99491) - MZChange and float(compareIon) < (float(currentIon) + 27.99491) + MZChange or \
                           float(currentIon) > (float(compareIon) + 27.99491) - MZChange and float(currentIon) < (float(compareIon) + 27.99491) + MZChange:
                            hitDetect = 1
                            #filterList[n1][0] = mFNum                            
                            if filterList[n1][4] == 1:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-CO-H]-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M-H]-"
                            else:
                                filterList[smallerIonRow][6] = str(filterList[smallerIonRow][6]) + "[M-CO" + str(int(filterList[smallerIonRow][4])) + "H]" + str(filterList[smallerIonRow][4]) + "-"
                                filterList[largerIonRow][6] = str(filterList[largerIonRow][6]) + "[M-" + str(int(filterList[largerIonRow][4])) + "H]" + str(filterList[largerIonRow][4]) + "-"
                            #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")
                            #print ("[M-CO-H] _ " + str(currentIon) + " _ " + str(compareIon))
                            #print filterList[n1]


                        #1525.510966([M-CO-H]-) -----> 1553.505441([M-H]-)
                        #1581.501053([M-H]-) -----> 1553.505441([M-H]-[M-CO-H]-)
                        #1581.501053([M-H]-[M-CO-H]-) -----> 1609.49482([M-H]-)    ##### But 1525.5 was not in moelcular feature


                        #elif float(compareIon) > (float(currentIon) + 96.96012) - MZChange and float(compareIon) < (float(currentIon) + 96.96012) + MZChange or \  #####Check mass diff. calc.
                        #   float(currentIon) > (float(compareIon) + 96.96012) - MZChange and float(currentIon) < (float(compareIon) + 96.96012) + MZChange:
                        #    filterList[n1][0] = mFNum
                        #    if currentIon < compareIon:
                        #        filterList[n][6] = str(filterList[n][6]) + "[M-" + str(filterList[n][4]) + "H]" + str(filterList[n][4]) + "-"
                        #        filterList[n1][6] = str(filterList[n1][6]) + "[M+SO4H-"  + str(filterList[n1][4]) + "H]" + str(filterList[n1][4]) + "-"
                        #    else:
                        #        filterList[n1][6] = str(filterList[n1][6]) + "[M-" + str(filterList[n1][4]) + "H]" + str(filterList[n1][4]) + "-"
                        ##        filterList[n][6] = str(filterList[n][6]) + "[M+SO4H-"  + str(filterList[n1][4]) + "H]" + str(filterList[n][4]) + "-"
                        #    print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ")")

                    if hitDetect == 1:
                        #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ") ____ " + str(filterList[n][0]))
                        if filterList[n1][0] == 0:
                            filterList[n1][0] = mFNum
                        else:
                            changeMFNum = filterList[n1][0]
                            while n2 < len(filterList):
                                if filterList[n2][0] == changeMFNum:
                                    filterList[n2][0] = mFNum
                                n2 = n2 + 1
                            n2 = 0
                        hitDetect = 0

                n1 = n1 + 1

            n = n + 1
            n1 = 0

        n = 0
        n1 = 1
        n2 = 0
        hitDetect = 0

        #Loop to search for the mass difference between a double charged ion and adducts of the single charged ion
        #print ("------Mataching double and triple charges---------")
        
        while n < len(filterList):

            if int(filterList[n][4]) > 1:
                if detectorPolarity == "Positive":
                    currentIon = float(filterList[n][1]) * float(filterList[n][4]) - (1.00727 * (float(filterList[n][4]) - 1))
                else:
                    currentIon = float(filterList[n][1]) * float(filterList[n][4]) + (1.00727 * (float(filterList[n][4]) - 1))
                MZChange = currentIon / 1000000 * ppmError
                currentRT = filterList[n][2]
                mFNum = filterList[n][0]
            else:
                n1 = len(filterList)
            
            while n1 < len(filterList):

                if int(filterList[n1][4]) > 1:
                    if detectorPolarity == "Positive":
                        compareIon = float(filterList[n1][1]) * float(filterList[n1][4]) - (1.00727 * (float(filterList[n1][4]) - 1))
                    else:
                        compareIon = float(filterList[n1][1]) * float(filterList[n1][4]) + (1.00727 * (float(filterList[n1][4]) - 1))

                ##compareIon = float(filterList[n1][1])
                
                if float(filterList[n1][2]) < (currentRT + RTChange) and \
                        float(filterList[n1][2]) > (currentRT - RTChange):

##                    smallerIonRow = n
##                    largerIonRow = n1
##                    if float(currentIon) > float(compareIon):
##                        largerIonRow = n
##                        smallerIonRow = n1

                    if detectorPolarity == "Positive" and filterList[n1][4] != filterList[n][4]: ##filterList[n1][4] == 1:

                    #if float(filterList[n1][4]) == 1:

                        if float(compareIon) > (float(currentIon) + 18.01057) - MZChange and float(compareIon) < (float(currentIon) + 18.01057) + MZChange or \
                           float(currentIon) > (float(compareIon) + 18.01057) - MZChange and float(currentIon) < (float(compareIon) + 18.01057) + MZChange:
                            hitDetect = 1
                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+H]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M-H2O+" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "+"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M-H2O+H]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "+"
                            #print ("2H - H2O-M _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1]))
                            
                        elif float(compareIon) > (float(currentIon) + 17.02655) - MZChange and float(compareIon) < (float(currentIon) + 17.02655) + MZChange or \
                           float(currentIon) > (float(compareIon) + 17.02655) - MZChange and float(currentIon) < (float(compareIon) + 17.02655) + MZChange:
                            hitDetect = 1
                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+NH4]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "+"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+H]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+NH4+" + str(int(filterList[n][4])-1) + "H]" + str(filterList[n][4]) + "+"
                            #print ("2H - M-NH4 _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1]))

                        elif float(compareIon) > (float(currentIon)) - MZChange and float(compareIon) < (float(currentIon)) + MZChange: # or \
                           #float(currentIon) > (float(compareIon)) - MZChange and float(currentIon) < (float(compareIon)) + MZChange:
                            hitDetect = 1
                            filterList[n1][6] = str(filterList[n1][6]) + "[M+H]+"
                            filterList[n][6] = str(filterList[n][6]) + "[M+" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "+"
                            #print ("2H - M _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1]))
                            
                        elif float(compareIon) > (float(currentIon) + 4.95539) - MZChange and float(compareIon) < (float(currentIon) + 4.95539) + MZChange or \
                           float(currentIon) > (float(compareIon) + 4.95539) - MZChange and float(currentIon) < (float(compareIon) + 4.95539) + MZChange:
                            hitDetect = 1
                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+Na]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+NH4+" + str(int(filterList[n][4])-1) + "H]" + str(filterList[n][4]) + "+"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+NH4]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+Na+" + str(int(filterList[n][4])-1) + "H]" + str(filterList[n][4]) + "+"
                            #print ("2H - NH4-Na _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1]))
                            
                        elif float(compareIon) > (float(currentIon) + 15.97394) - MZChange and float(compareIon) < (float(currentIon) + 15.97394) + MZChange or \
                           float(currentIon) > (float(compareIon) + 15.97394) - MZChange and float(currentIon) < (float(compareIon) + 15.97394) + MZChange:
                            hitDetect = 1
                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+K]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+Na+" + str(int(filterList[n][4])-1) + "H]" + str(filterList[n][4]) + "+"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+Na]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+K+" + str(int(filterList[n][4])-1) + "H]" + str(filterList[n][4]) + "+"
                            #print ("2H - Na-K _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1]))
                            
                        elif float(compareIon) > (float(currentIon) + 35.03712) - MZChange and float(compareIon) < (float(currentIon) + 35.03712) + MZChange or \
                           float(currentIon) > (float(compareIon) + 35.03712) - MZChange and float(currentIon) < (float(compareIon) + 35.03712) + MZChange:
                            hitDetect = 1
                            #print ("2H - H2O-NH4 _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1]))
                            
                        elif float(compareIon) > (float(currentIon) + 21.98194) - MZChange and float(compareIon) < (float(currentIon) + 21.98194) + MZChange or \
                           float(currentIon) > (float(compareIon) + 21.98194) - MZChange and float(currentIon) < (float(compareIon) + 21.98194) + MZChange:
                            hitDetect = 1
                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+Na]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "+"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+H]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+Na+" + str(int(filterList[n][4])-1) + "H]" + str(filterList[n][4]) + "+"
                            #print ("2H - M-Na _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1]))
                            
                        elif float(compareIon) > (float(currentIon) + 20.92933) - MZChange and float(compareIon) < (float(currentIon) + 20.92933) + MZChange or \
                           float(currentIon) > (float(compareIon) + 20.92933) - MZChange and float(currentIon) < (float(compareIon) + 20.92933) + MZChange:
                            hitDetect = 1
                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+K]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+NH4+" + str(int(filterList[n][4])-1) + "H]" + str(filterList[n][4]) + "+"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+NH4]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+K+" + str(int(filterList[n][4])-1) + "H]" + str(filterList[n][4]) + "+"
                            #print ("2H - NH4-K _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1]))
                            
                        elif float(compareIon) > (float(currentIon) + 39.99251) - MZChange and float(compareIon) < (float(currentIon) + 39.99251) + MZChange or \
                           float(currentIon) > (float(compareIon) + 39.99251) - MZChange and float(currentIon) < (float(compareIon) + 39.99251) + MZChange:
                            hitDetect = 1
                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+Na]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M-H2O+" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "+"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M-H2O+H]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+Na+" + str(int(filterList[n][4])-1) + "H]" + str(filterList[n][4]) + "+"
                            #print ("2H - H2O-Na _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1]))
                            
                        elif float(compareIon) > (float(currentIon) + 37.95588) - MZChange and float(compareIon) < (float(currentIon) + 37.95588) + MZChange or \
                           float(currentIon) > (float(compareIon) + 37.95588) - MZChange and float(currentIon) < (float(compareIon) + 37.95588) + MZChange:
                            hitDetect = 1
                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+K]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "+"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+H]+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+K+" + str(int(filterList[n][4])-1) + "H]" + str(filterList[n][4]) + "+"
                            #print ("2H - M-K _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1]))
                            
                        elif float(compareIon) > (float(currentIon) + 55.96645) - MZChange and float(compareIon) < (float(currentIon) + 55.96645) + MZChange or \
                           float(currentIon) > (float(compareIon) + 55.96645) - MZChange and float(currentIon) < (float(compareIon) + 55.96645) + MZChange:
                            hitDetect = 1
                            
                            #print ("2H - H2O-K _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1]))

                    elif filterList[n1][4] == 1:

                        if float(compareIon) > (float(currentIon)) - MZChange and float(compareIon) < (float(currentIon)) + MZChange: # or \
##                           float(currentIon) > (float(compareIon)) - MZChange and float(currentIon) < (float(compareIon)) + MZChange:
                            hitDetect = 1
                            filterList[n1][6] = str(filterList[n1][6]) + "[M-H]-"
                            filterList[n][6] = str(filterList[n][6]) + "[M-" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "-"
                            #print ("2H - M _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1]))

                        elif float(compareIon) > (float(currentIon) + 18.01057) - MZChange and float(compareIon) < (float(currentIon) + 18.01057) + MZChange or \
                           float(currentIon) > (float(compareIon) + 18.01057) - MZChange and float(currentIon) < (float(compareIon) + 18.01057) + MZChange:
                            hitDetect = 1
                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M-H]-"
                                filterList[n][6] = str(filterList[n][6]) + "[M-H2O-" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "-"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M-H2O-H]-"
                                filterList[n][6] = str(filterList[n][6]) + "[M-" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "-"
                            #print ("2H - H2O-M _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1]))

                        elif float(compareIon) > (float(currentIon) + 27.99491) - MZChange and float(compareIon) < (float(currentIon) + 27.99491) + MZChange or \
                           float(currentIon) > (float(compareIon) + 27.99491) - MZChange and float(currentIon) < (float(compareIon) + 27.99491) + MZChange:
                            hitDetect = 1
                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M-H]-"
                                filterList[n][6] = str(filterList[n][6]) + "[M-CO-" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "-"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M-CO-H]-"
                                filterList[n][6] = str(filterList[n][6]) + "[M-" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "-"

                    if hitDetect == 1:
                        mFNum = filterList[n][0]
                        #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ") ____ " + str(filterList[n][0]))
                        
                        if filterList[n1][0] == 0:
                            filterList[n1][0] = mFNum
                        else:
                            changeMFNum = filterList[n1][0]
                            while n2 < len(filterList):
                                if filterList[n2][0] == changeMFNum:
                                    filterList[n2][0] = mFNum
                                n2 = n2 + 1
                            n2 = 0
                        hitDetect = 0

                n1 = n1 + 1

            n = n + 1
            n1 = 0

        n = 0
        n1 = 1
        n2 = 0
        hitDetect = 0

        #print ("------Mataching dimers---------")

        #Loop to search for the mass difference between a dimer and adducts of the monomer 
        while n < len(filterList):

            if filterList[n][4] != 0 and filterList[n][0] != 0:

                #currentIon = (float(filterList[n][1]) * float(filterList[n][4]) - (1.00727 * (float(filterList[n][4]) - 1)))                
                currentIon = (float(filterList[n][1])) / 2 + (1.00727 / 2)
                MZChange = currentIon / 1000000 * ppmError
                currentRT = filterList[n][2]
                mFNum = filterList[n][0]
                
            else:
                
                n1 = len(filterList)
            
            while n1 < len(filterList):

                #compareIon = ((float(filterList[n1][1]) * float(filterList[n1][4]) - (1.00727 * (float(filterList[n1][4]) - 1))) - 1.00727) / 2 + 1.00727
                compareIon = float(filterList[n1][1])
                
                if float(filterList[n1][2]) < (currentRT + RTChange) and \
                        float(filterList[n1][2]) > (currentRT - RTChange) and filterList[n][4] == filterList[n1][4]:

                    if detectorPolarity == "Positive":

                        if float(compareIon) > (float(currentIon) + 18.01057) - MZChange and float(compareIon) < (float(currentIon) + 18.01057) + MZChange or \
                           float(currentIon) > (float(compareIon) + 18.01057) - MZChange and float(currentIon) < (float(compareIon) + 18.01057) + MZChange:
                            hitDetect = 1

                            #print "2M - H2O-M _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
                            
                        elif float(compareIon) > (float(currentIon) + 17.02655) - MZChange and float(compareIon) < (float(currentIon) + 17.02655) + MZChange or \
                           float(currentIon) > (float(compareIon) + 17.02655) - MZChange and float(currentIon) < (float(compareIon) + 17.02655) + MZChange:
                            hitDetect = 1

                            #print "2M - M-NH4 _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])

                        elif float(compareIon) > (float(currentIon)) - MZChange and float(compareIon) < (float(currentIon)) + MZChange or \
                           float(currentIon) > (float(compareIon)) - MZChange and float(currentIon) < (float(compareIon)) + MZChange:
                            hitDetect = 1

                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[2M+" + str(int(filterList[n1][4])) + "H]" + str(filterList[n1][4]) + "+"
                                filterList[n][6] = str(filterList[n][6]) + "[M+" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "+"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+" + str(int(filterList[n1][4])) + "H]" + str(filterList[n1][4]) + "+"
                                filterList[n][6] = str(filterList[n][6]) + "[2M+" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "+"

                            #print "2M - M _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
                            
    ##                    elif float(compareIon) > (float(currentIon) + 2.4776949) - MZChange and float(compareIon) < (float(currentIon) + 2.4776949) + MZChange or \
    ##                       float(currentIon) > (float(compareIon) + 2.4776949) - MZChange and float(currentIon) < (float(compareIon) + 2.4776949) + MZChange:
    ##                        hitDetect = 1
    ##
    ##                        #print "2M - NH4-Na _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
    ##                        
    ##                    elif float(compareIon) > (float(currentIon) + 7.98697) - MZChange and float(compareIon) < (float(currentIon) + 7.98697) + MZChange or \
    ##                       float(currentIon) > (float(compareIon) + 7.98697) - MZChange and float(currentIon) < (float(compareIon) + 7.98697) + MZChange:
    ##                        hitDetect = 1
    ##
    ##                        #print "2M - Na-K _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
    ##                        
    ##                    elif float(compareIon) > (float(currentIon) + 17.51856) - MZChange and float(compareIon) < (float(currentIon) + 17.51856) + MZChange or \
    ##                       float(currentIon) > (float(compareIon) + 17.51856) - MZChange and float(currentIon) < (float(compareIon) + 17.51856) + MZChange:
    ##                        hitDetect = 1
    ##
    ##                        #print "2M - H2O-NH4 _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
    ##                        
                        elif float(compareIon) > (float(currentIon) + 21.98194) - MZChange and float(compareIon) < (float(currentIon) + 21.98194) + MZChange or \
                           float(currentIon) > (float(compareIon) + 21.98194) - MZChange and float(currentIon) < (float(compareIon) + 21.98194) + MZChange:
                            hitDetect = 1
                                
                            #print "2M - M-Na _ " + str(currentIon) + " _ " + str(compareIon)
    ##                        
    ##                    elif float(compareIon) > (float(currentIon) + 10.464665) - MZChange and float(compareIon) < (float(currentIon) + 10.464665) + MZChange or \
    ##                       float(currentIon) > (float(compareIon) + 10.464665) - MZChange and float(currentIon) < (float(compareIon) + 10.464665) + MZChange:
    ##                        hitDetect = 1
    ##                        
    ##                        #print "2M - NH4-K _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
    ##                        
    ##                    elif float(compareIon) > (float(currentIon) + 19.996255) - MZChange and float(compareIon) < (float(currentIon) + 19.996255) + MZChange or \
    ##                       float(currentIon) > (float(compareIon) + 19.996255) - MZChange and float(currentIon) < (float(compareIon) + 19.996255) + MZChange:
    ##                        hitDetect = 1
    ##
    ##                        #print "2M - H2O-Na _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
    ##                        
                        elif float(compareIon) > (float(currentIon) + 37.95588) - MZChange and float(compareIon) < (float(currentIon) + 37.95588) + MZChange or \
                           float(currentIon) > (float(compareIon) + 37.95588) - MZChange and float(currentIon) < (float(compareIon) + 37.95588) + MZChange:
                            hitDetect = 1

                            #print "2M - M-K _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
                            
    ##                    elif float(compareIon) > (float(currentIon) + 27.983225) - MZChange and float(compareIon) < (float(currentIon) + 27.983225) + MZChange or \
    ##                       float(currentIon) > (float(compareIon) + 27.983225) - MZChange and float(currentIon) < (float(compareIon) + 27.983225) + MZChange:
    ##                        hitDetect = 1
    ##                        
    ##                        #print "2M - H2O-K _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])


                    else:


                        if float(compareIon) > (float(currentIon) + 18.01057) - MZChange and float(compareIon) < (float(currentIon) + 18.01057) + MZChange or \
                           float(currentIon) > (float(compareIon) + 18.01057) - MZChange and float(currentIon) < (float(compareIon) + 18.01057) + MZChange:
                            hitDetect = 1

                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[2M-" + str(int(filterList[n1][4])) + "H]" + str(filterList[n1][4]) + "-"
                                filterList[n][6] = str(filterList[n][6]) + "[M-H2O-" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "-"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M-H2O-" + str(int(filterList[n1][4])) + "H]" + str(filterList[n1][4]) + "-"
                                filterList[n][6] = str(filterList[n][6]) + "[2M-" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "-"

                            #print "2M - H2O-M _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
                            
                        elif float(compareIon) > (float(currentIon) + 17.02655) - MZChange and float(compareIon) < (float(currentIon) + 17.02655) + MZChange or \
                           float(currentIon) > (float(compareIon) + 17.02655) - MZChange and float(currentIon) < (float(compareIon) + 17.02655) + MZChange:
                            hitDetect = 1

                            #print "2M - M-NH4 _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])

                        elif float(compareIon) > (float(currentIon)) - MZChange and float(compareIon) < (float(currentIon)) + MZChange or \
                           float(currentIon) > (float(compareIon)) - MZChange and float(currentIon) < (float(compareIon)) + MZChange:
                            hitDetect = 1

                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[2M-" + str(int(filterList[n1][4])) + "H]" + str(filterList[n1][4]) + "-"
                                filterList[n][6] = str(filterList[n][6]) + "[M-" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "-"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M-" + str(int(filterList[n1][4])) + "H]" + str(filterList[n1][4]) + "-"
                                filterList[n][6] = str(filterList[n][6]) + "[2M-" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "-"

                            #print "2M - M _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
                            
    ##                    elif float(compareIon) > (float(currentIon) + 2.4776949) - MZChange and float(compareIon) < (float(currentIon) + 2.4776949) + MZChange or \
    ##                       float(currentIon) > (float(compareIon) + 2.4776949) - MZChange and float(currentIon) < (float(compareIon) + 2.4776949) + MZChange:
    ##                        hitDetect = 1
    ##
    ##                        #print "2M - NH4-Na _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
    ##                        
    ##                    elif float(compareIon) > (float(currentIon) + 7.98697) - MZChange and float(compareIon) < (float(currentIon) + 7.98697) + MZChange or \
    ##                       float(currentIon) > (float(compareIon) + 7.98697) - MZChange and float(currentIon) < (float(compareIon) + 7.98697) + MZChange:
    ##                        hitDetect = 1
    ##
    ##                        #print "2M - Na-K _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
    ##                        
    ##                    elif float(compareIon) > (float(currentIon) + 17.51856) - MZChange and float(compareIon) < (float(currentIon) + 17.51856) + MZChange or \
    ##                       float(currentIon) > (float(compareIon) + 17.51856) - MZChange and float(currentIon) < (float(compareIon) + 17.51856) + MZChange:
    ##                        hitDetect = 1
    ##
    ##                        #print "2M - H2O-NH4 _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
    ##                        
                        elif float(compareIon) > (float(currentIon) + 21.98194) - MZChange and float(compareIon) < (float(currentIon) + 21.98194) + MZChange or \
                           float(currentIon) > (float(compareIon) + 21.98194) - MZChange and float(currentIon) < (float(compareIon) + 21.98194) + MZChange:
                            hitDetect = 1
                                
                            #print "2M - M-Na _ " + str(currentIon) + " _ " + str(compareIon)
    ##                        
    ##                    elif float(compareIon) > (float(currentIon) + 10.464665) - MZChange and float(compareIon) < (float(currentIon) + 10.464665) + MZChange or \
    ##                       float(currentIon) > (float(compareIon) + 10.464665) - MZChange and float(currentIon) < (float(compareIon) + 10.464665) + MZChange:
    ##                        hitDetect = 1
    ##                        
    ##                        #print "2M - NH4-K _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
    ##                        
    ##                    elif float(compareIon) > (float(currentIon) + 19.996255) - MZChange and float(compareIon) < (float(currentIon) + 19.996255) + MZChange or \
    ##                       float(currentIon) > (float(compareIon) + 19.996255) - MZChange and float(currentIon) < (float(compareIon) + 19.996255) + MZChange:
    ##                        hitDetect = 1
    ##
    ##                        #print "2M - H2O-Na _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
    ##                        
                        elif float(compareIon) > (float(currentIon) + 37.95588) - MZChange and float(compareIon) < (float(currentIon) + 37.95588) + MZChange or \
                           float(currentIon) > (float(compareIon) + 37.95588) - MZChange and float(currentIon) < (float(compareIon) + 37.95588) + MZChange:
                            hitDetect = 1

                            #print "2M - M-K _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])
                            
    ##                    elif float(compareIon) > (float(currentIon) + 27.983225) - MZChange and float(compareIon) < (float(currentIon) + 27.983225) + MZChange or \
    ##                       float(currentIon) > (float(compareIon) + 27.983225) - MZChange and float(currentIon) < (float(compareIon) + 27.983225) + MZChange:
    ##                        hitDetect = 1
    ##                        
    ##                        #print "2M - H2O-K _ " + str(filterList[n][1]) + " _ " + str(filterList[n1][1])

                        elif float(compareIon) > (float(currentIon) + 46.00547) - MZChange and float(compareIon) < (float(currentIon) + 46.00547) + MZChange or \
                           float(currentIon) > (float(compareIon) + 46.00547) - MZChange and float(currentIon) < (float(compareIon) + 46.00547) + MZChange:
                            hitDetect = 1

                            if compareIon > currentIon:
                                filterList[n1][6] = str(filterList[n1][6]) + "[2M-" + str(int(filterList[n1][4])) + "H]" + str(filterList[n1][4]) + "-"
                                filterList[n][6] = str(filterList[n][6]) + "[M+CHOOH-" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "-"
                            else:
                                filterList[n1][6] = str(filterList[n1][6]) + "[M+CHOOH-" + str(int(filterList[n1][4])) + "H]" + str(filterList[n1][4]) + "-"
                                filterList[n][6] = str(filterList[n][6]) + "[2M-" + str(int(filterList[n][4])) + "H]" + str(filterList[n][4]) + "-"

                    if hitDetect == 1:
                        #print (str(filterList[n][1]) + "(" + filterList[n][6] + ")" + " -----> " + str(filterList[n1][1]) + "(" + filterList[n1][6] + ") ____ " + str(filterList[n][0]))
                        if filterList[n1][0] == 0:
                            filterList[n1][0] = mFNum
                        else:
                            changeMFNum = filterList[n1][0]
                            while n2 < len(filterList):
                                if filterList[n2][0] == changeMFNum:
                                    filterList[n2][0] = mFNum
                                n2 = n2 + 1
                            n2 = 0
                        hitDetect = 0

                n1 = n1 + 1

            n = n + 1
            n1 = 0
            
        primary.masterList = filterList

        #print(filterList)


        primary.txt.configure(state="normal")
        primary.txt.delete(1.0, END)
        primary.txt.insert('1.0', "Your current samples chemical and molecular features have been compiled" + '\n')
        primary.txt.configure(state="disabled")
            
        return

    def applyFilter(primary):
        
        filterList = primary.masterList
        filterMode = primary.selectedMode.get()
        areaCutOff = float(primary.areaVar.get())
        #minRT = float(primary.minRTVar.get())
        minRT = 0
        minHitRate = float(primary.requireVar.get())
        currentMode = primary.selectedFeature.get()
        
        n = 0
        n1 = 1
        resultList = []
        i = 0
        
        listForID = []
        listForMZ = []
        listForRT = []
        listForPA = []
        comboList = []
        MFList = []
        testMF = 0
        tempTestMF = ""
        tempTestMFCharge = ""
        tempCurrentMF = ""
        testMFAll = ""
        
        currentMF = 0
        currentMFCharge = ""
        ID = 0
        PA = 0
        MZ = 0
        RT = 0
        counter = 0
        missingA2 = 0
                
        peakA1 = 0
        peakA2 = 0
        peakA3 = 0
        massA1 = 0
        massA2 = 0
        massA3 = 0
        isotopeCount = 0
        peakCompare3 = 0
        peakCompare2 = 0
        maxCompare2 = 0
        minCompare2 = 0
        maxCompare3 = 0
        minCompare3 = 0
        minMassComp = 0
        maxMassComp = 0
        maxPeakComp = 0
        minPeakComp = 0
        massCompare = 0
        massCompareA1 = 0
        sulphMinPeakComp = 0

        n = 0
        haloHit = 0
        
        while n < len(filterList):
            peakA1 = float(filterList[n][3])
            if float(filterList[n][4]) != 0:
                massA1 = (float(filterList[n][1])*float(filterList[n][4]))-((float(filterList[n][4])-1)*1.00728)

                if filterList[n][5].count(':') > 1:

                    isotopeCount = filterList[n][5].count(':')
                    
                    peakA2 = filterList[n][5]
                    peakA2 = peakA2.split(':')
                    peakA2 = peakA2[0]
                    peakA2 = peakA2.split('-')
                    peakA2 = peakA2[2]

                    peakA3 = filterList[n][5]
                    peakA3 = peakA3.split(':')
                    peakA3 = peakA3[1]
                    peakA3 = peakA3.split('-')
                    peakA3 = peakA3[2]

                    massA1 = (float(filterList[n][1])*float(filterList[n][4]))-((float(filterList[n][4])-1)*1.00728)

                    massA2 = filterList[n][5]
                    massA2 = massA2.split(':')
                    massA2 = massA2[0]
                    massA2 = massA2.split('-')
                    massA2 = (float(massA2[0])*float(filterList[n][4]))-((float(filterList[n][4])-1)*1.00728)

                    massA3 = filterList[n][5]
                    massA3 = massA3.split(':')
                    massA3 = massA3[1]
                    massA3 = massA3.split('-')
                    massA3 = (float(massA3[0])*float(filterList[n][4]))-((float(filterList[n][4])-1)*1.00728)

##                    if float(massA3)-float(massA2) > 1.5:
##
##                        peakCompare3 = float(peakA2)/float(peakA1)
##                        massCompare = float(massA2)-float(massA1)
##                        massCompareA1 = float(massA2)-float(massA1)
##                        missingA2 = 1
##
##                    else:
##
##                        peakCompare3 = float(peakA3)/float(peakA1)
##                        massCompare = float(massA3)-float(massA2)
##                        massCompareA1 = float(massA2)-float(massA1)
##                        missingA2 = 0

                    peakCompare3 = float(peakA3)/float(peakA1)
                    massCompare = float(massA3)-float(massA2)
                    massCompareA1 = float(massA2)-float(massA1)

                    minMassComp = 0
                    maxMassComp = 0

                    if "0-0-0" in str(filterList[n][5]):
                        filterList[n][5] = str.replace(str(filterList[n][5]),"0-0-0:","")
                    
                    if filterMode == "DCA-Hal":

                        maxPeakComp = 1.611 * 10**(-7) * float(massA1)**2 - 1.319 * 10**(-5) * float(massA1) + 12.05
                        minPeakComp = 1.611 * 10**(-7) * float(massA1)**2 - 1.319 * 10**(-5) * float(massA1) + 0.2702 #Original 5% Error
                        
                        maxMassComp = 1.5644 * 10**(-23) * float(massA1)**6 - 2.46 * 10**(-19) * float(massA1)**5 + 1.5135 * 10**(-15) * float(massA1)**4 - \
                            4.485 * 10**(-12) * float(massA1)**3 + 5.954 * 10**(-9) * float(massA1)**2 - 9.019 * 10**(-7) * float(massA1) + 0.99832
                        minMassComp = 0.9936 - (float(massA1) / 1000000 * 5)

                        primary.filterMode = "DCA-Hal"

                    elif  filterMode == "DCA-Sul":

                        maxPeakComp = 1.611 * 10**(-7) * float(massA1)**2 - 1.319 * 10**(-5) * float(massA1) + 0.2702 #Original 5% Error
                        minPeakComp = 1.611 * 10**(-7) * float(massA1)**2 - 7.982 * 10**(-6) * float(massA1) + 0.00471
                        
                        maxMassComp = 4.288 * 10**(-23) * float(massA1)**6 - 4.975 * 10**(-19) * float(massA1)**5 + 2.0086 * 10**(-15) * float(massA1)**4 - \
                            2.735 * 10**(-12) * float(massA1)**3 - 2.07 * 10**(-9) * float(massA1)**2 + 8.454 * 10**(-6) * float(massA1) + 0.99684
                        minMassComp = 0.9936 - (float(massA1) / 1000000 * 5)

                        primary.filterMode = "DCA-Sul"

                    elif  filterMode == "DCA-C":

                        maxPeakComp = 1.611 * 10**(-7) * float(massA1)**2 - 1.319 * 10**(-5) * float(massA1) + 0.2702
                        minPeakComp = 0.0005

                        maxMassComp = 1.006
                        minMassComp = 4.288 * 10**(-23) * float(massA1)**6 - 4.975 * 10**(-19) * float(massA1)**5 + 2.0086 * 10**(-15) * float(massA1)**4 - \
                            2.735 * 10**(-12) * float(massA1)**3 - 2.07 * 10**(-9) * float(massA1)**2 + 8.454 * 10**(-6) * float(massA1) + 0.99684

                        primary.filterMode = "DCA-C"

                    elif  filterMode == "DCA-Bor":

                        maxPeakComp = 100
                        minPeakComp = 0

                        if float(massA1) < 2000:
                            maxMassComp = -0.0000000008575*float(massA1)**2+0.000004535*float(massA1) +0.996
                        else:
                            maxMassComp = float(massA1)*0.00000108+0.9995

                        minMassComp = 0.995
                        massCompare = massCompareA1

                        primary.filterMode = "DCA-Bor"

                    if filterMode == "All Features":
                        if currentMode == "Molecular":
                            resultList.append(str(filterList[n][0]) + ":" + str(filterList[n][4]) + "_" + str(filterList[n][1]) + "-" + str(filterList[n][2]) + \
                                    "-" + str(filterList[n][3]) + ":" + str(filterList[n][5]))
                        else:
                            resultList.append(str(filterList[n][4]) + "+" + str(filterList[n][1]) + "-" + str(filterList[n][2]) + \
                                    "-" + str(filterList[n][3]) + ":" + str(filterList[n][5]))
                        haloHit == 1

                        primary.filterMode = "All Features"
                        
                    elif haloHit == 0: #elif, if using All Features
                        if peakCompare3 < maxPeakComp:
                            if peakCompare3 > minPeakComp:
                                if massCompare < maxMassComp:
                                    if massCompare > minMassComp:
                                        if currentMode == "Molecular":
                                            resultList.append(str(filterList[n][0]) + ":" + str(filterList[n][4]) + "_" + str(filterList[n][1]) + "-" + str(filterList[n][2]) + \
                                                    "-" + str(filterList[n][3]) + ":" + str(filterList[n][5]))
                                        else:
                                            resultList.append(str(filterList[n][4]) + "+" + str(filterList[n][1]) + "-" + str(filterList[n][2]) + \
                                                    "-" + str(filterList[n][3]) + ":" + str(filterList[n][5]))
                                        #print(filterList[n])
                                        haloHit = 1
                                        
                    #Use below to invert results. Also need to remove the results appended above....
                    #if haloHit == 0:
                        #resultList.append(str(filterList[n][1]) + "-" + str(filterList[n][2]) + \
                                #"-" + str(filterList[n][3]) + ":" + str(filterList[n][5]))
                    
            haloHit = 0
            n = n + 1

        #print(resultList)

        if currentMode == "Molecular":

            n = 0
            n1 = 1
            totalNumFromFilter = 1
            
            while n < len(resultList):
                #print(resultList[n])
                currentMF = resultList[n]
                currentMF = currentMF.split('_')
                currentMF = currentMF[0]
                currentMF = currentMF.split(':')
                currentMFCharge = currentMF[1]
                currentMF = currentMF[0]
                    
                while n1 < len(resultList):
                    testMF = resultList[n1]
                    testMF = testMF.split('_')
                    testMF = testMF[0]
                    testMF = testMF.split(':')
                    testMF = testMF[0]
                    
                    if testMF == currentMF:

                        tempTestMF = resultList[n1]
                        tempTestMF = tempTestMF.split('_')
                        tempTestMF = tempTestMF[1]
                        tempTestMFCharge = resultList[n1]
                        tempTestMFCharge = tempTestMFCharge.split(':')
                        tempTestMFCharge = tempTestMFCharge[1]
                        tempTestMFCharge = tempTestMFCharge.split('_')
                        tempTestMFCharge = tempTestMFCharge[0]
                        
                        testMFAll = testMFAll + tempTestMFCharge + "+" + tempTestMF
                        resultList[n1] = "0:0_0-0-0:"
                        totalNumFromFilter = totalNumFromFilter + 1

                    n1 = n1 + 1
                
                if float(currentMF) > 0:
                    tempCurrentMF = resultList[n]
                    MFList.append(str(totalNumFromFilter) + "+" + currentMFCharge + "+" + tempCurrentMF.split(':')[0] + "_" + tempCurrentMF.split('_')[1] + testMFAll)
                    
                testMFAll = ""
                totalNumFromFilter = 1
                
                n = n + 1
                n1 = n + 1

            resultList = MFList
            #print(resultList)

            n = 0
            n1 = 0
            totalNumInMF = 0
            probabilityOfHit = 0
            MissedCFList = []
            hitRateList = []
            
            #Loop through resultsList to compare molecular feature number to that of the filterList
            #to see if any chemical features were missed by the filter equations
            while n < len(resultList):

                currentMF = resultList[n]
                currentMF = currentMF.split('_')[0]
                currentMF = currentMF.split('+')[2]
                
                while n1 < len(filterList):

                    testMF = filterList[n1][0]
                    
                    if str(testMF) == str(currentMF):

                        totalNumInMF = totalNumInMF + 1
                        tempTestMF = (str(filterList[n1][4]) + "+" + str(filterList[n1][1]) + "-" + str(filterList[n1][2]) + \
                                    "-" + str(filterList[n1][3]) + ":" + str(filterList[n1][5]))
                        testMFAll = testMFAll + tempTestMF
                         
                    n1 = n1 + 1

                totalNumFromFilter = resultList[n]
                totalNumFromFilter = totalNumFromFilter.split('_')[0]
                totalNumFromFilter = totalNumFromFilter.split('+')[0]

                probabilityOfHit = float(totalNumFromFilter) / float(totalNumInMF) * 100
                probabilityOfHit = '%.1f' % (float(probabilityOfHit))

                if float(probabilityOfHit) >= minHitRate:
                    MissedCFList.append(testMFAll)
                    hitRateList.append(float(probabilityOfHit))
                
                n1 = 0
                n = n + 1
                testMFAll = ""
                totalNumFromFilter = 0
                totalNumInMF = 0

            resultList = MissedCFList

        

        n = 0
        n1 = 0 
        currentPA = 0
        currentMaxPA = 0
        isoNum = 0

        #print(resultList)

        #Loop sets all features which have a maximum peak area less than the cut off to 0
        while n < len(resultList):
            currentMaxPA = 0
            isoNum = resultList[n]
            isoNum = isoNum.split(':')
            isoNum = len(isoNum) - 1
            #print(resultList[n])
            #print(isoNum)

            while n1 < isoNum:
                currentPA = resultList[n]
                currentPA = currentPA.split(':')
                currentPA = currentPA[n1]
                currentPA = currentPA.split('-')
                currentPA = currentPA[2]
                
                if float(currentPA) > float(currentMaxPA):
                    currentMaxPA = currentPA
                
                n1 = n1 + 1
            
            if float(currentMaxPA) < float(areaCutOff):
                resultList[n] = 0
                if currentMode == "Molecular":
                    hitRateList[n] = 0

            n = n + 1
            n1 = 0

        n = 0
        n1 = 1
        currentRT = 0
        testRT = 0

        #Removed all features that are 0
        resultList[:] = (value for value in resultList if value != 0)

        if currentMode == "Molecular":
            hitRateList[:] = (value for value in hitRateList if value != 0)
        
        resultMZ = []
        resultRT = []
        resultPA = []
        final1 = []
        n = 0
        n1 = 0
        splitTheList = []
        completeRT = []
        currentAbund = 0
        testAbund = 0
        isotopeCount = 0
        printList = []
        i = 0
        pLCount = 0
        printList.append("0")

        while n < len(resultList):

            splitTheList = resultList[n]
            splitTheList = splitTheList.split(':')

            while n1 < (len(splitTheList)-1):
                testAbund = splitTheList[n1]
                testAbund = testAbund.split('-')
                testAbund = testAbund[2]
                
                if float(testAbund) > float(currentAbund):
                    currentAbund = testAbund
                    resultMZ = splitTheList[n1]
                    resultMZ = resultMZ.split('-')[0]
                    #resultMZ = resultMZ[0]
                    if "+" in resultMZ:
                        resultMZ = resultMZ.split('+')[1]
                    

                n1 = n1 + 1

            resultRT = resultList[n]
            resultRT = resultRT.split(':')
            resultRT = resultRT[0]
            resultRT = resultRT.split('-')
            resultRT = str('%.2f' % (float(resultRT[1])/60)) ##### HERE to change results to min for display #### All data imported from CSV should be in min, and converted to sec in the programme...

            completeRT.append(float(resultRT))
            
            resultPA = resultList[n]
            resultPA = resultPA.split(':')
            resultPA = resultPA[0]
            resultPA = resultPA.split('-')
            resultPA = resultPA[2]

            resultMZ = str(resultMZ) + ":" + str(resultRT) + ":" + str(resultPA)
            final1.append(resultMZ)

            testAbund = 0
            currentAbund = 0
            n1 = 0

            n = n + 1

        if len(final1) > 1:
            ## Sorts the two lists by RT
            if currentMode == "Molecular":
                completeRT, final1, resultList, hitRateList = zip(*sorted(zip(completeRT, final1, resultList, hitRateList)))
            else:
                completeRT, final1, resultList = zip(*sorted(zip(completeRT, final1, resultList)))

        
        
        simplifyRT = ""
        simplifyMZ = ""
        simplifyMZ1 = ""
        allMZ = ""
        ionChoices1 = []
        del ionChoices1[:]
        n = 0
        
        for each in final1:
            
            simplifyMZ = final1[n].split(':')
            simplifyMZ = simplifyMZ[0]
            if allMZ == "":
                allMZ = "Results for EIC: " + simplifyMZ
            else:
                allMZ = allMZ + "; " + simplifyMZ
            simplifyMZ = '%.1f' % (float(simplifyMZ))
            
            resultSimplify = final1[n].split(':')
            resultSimplify = resultSimplify[1]
            resultSimplify = float(resultSimplify) 
            resultSimplify = '%.2f' % (float(resultSimplify))
            
            ionChoices1.append(str(simplifyMZ) + " at " + str(resultSimplify))
            n = n + 1

        n = 0
        primary.txt.configure(state="normal")
        primary.txt.delete(1.0, END)

        primary.txt.insert('1.0', '\n' + allMZ)
        primary.txt.insert('1.0', '\n' + "-----------------------" + '\n')

        while n < len(final1):
            primary.txt.insert('1.0', str(final1[n]) + '\n')
            n = n + 1
            
        primary.txt.insert('1.0', "m/z:retention time:peak area" + '\n' +  '\n')
        primary.txt.configure(state="disabled")

        n = 0
        
        for each in ionChoices1:
            ionChoices1[n] = str(n+1) + ": " + str(ionChoices1[n]) + " min"
            n = n + 1

        if len(ionChoices1) == 0:
            ionChoices1.append("None Detected")
            
        #print(resultList)
        primary.sepOptions.set(ionChoices1[0])
        primary.sepOptions["values"] = ionChoices1
        primary.resultsMasterList = resultList
        if currentMode == "Molecular":
            primary.resultsMasterRateList = hitRateList
        
        return
    
    def exportAsCSV(primary):
        
        defualtFileName = primary.currentFileName
        defualtFileName = defualtFileName[:-4]
        defualtFileName = defualtFileName + "_" + primary.filterMode
        fileSaveName = filedialog.asksaveasfile(mode="w", initialfile=defualtFileName, defaultextension=".csv", filetypes=[('csv (Comma delimited)', '*.csv')])
        resultsForSave = copy.deepcopy(primary.resultsMasterList)

        chargeState = ""

        if fileSaveName != None:
        
            eachList = []
            isoList = []
            isoStr = ""
            eachListList = []
            eachStr = ""
            n = 0
            n1 = 0

            for each in resultsForSave:
                eachStr = each
                eachStr = eachStr[:-1]
                
                n = n + 1
                if n == 1:
                    eachStr = "ID-m/z-RT-Area-Charge:"+ eachStr 
                eachList = eachStr.split(':')
                
                for isos in eachList:
                    isoStr = isos
                    
                    n1 = n1 + 1
                    if n1 != 1:
                        isoStr = str(isoStr.split("-")[0]) + "-" + str('%.2f' % (float(isoStr.split("-")[1])/60)) + "-" + str(isoStr.split("-")[2]) 
                        isoStr = str(n) + "-" + isoStr
                    isoList = isoStr.split('-')
                    if "+" in isoList[1]:
                        chargeState = isoList[1].split("+")[0]
                        isoList[1] = isoList[1].split("+")[1]
                    isoList.append(chargeState)
                    eachListList.append(isoList)

            writer = csv.writer(fileSaveName, lineterminator='\n')
            writer.writerows(eachListList)
                
            fileSaveName.close()

        return

    def grph(primary, event):

        currentMode = primary.selectedFeature.get()
        resultsForPrint = []
        resultsForPrint = copy.deepcopy(primary.resultsMasterList)
        filtetedList = []

        if currentMode == "Molecular":
            rateList = []
            rateList = copy.deepcopy(primary.resultsMasterRateList)
            selectedRate = 0
        
        selectedResult = primary.selectedSep.get()

        if selectedResult == "NA":
            return
        elif selectedResult == "None Detected":
            return
        
        selectedResult = selectedResult.split(':')
        selectedResult = selectedResult[0]
        selectedResult = int(selectedResult) - 1

        filtetedList.append(resultsForPrint[int(selectedResult)])

        if currentMode == "Molecular":
            selectedRate = rateList[int(selectedResult)]

        massList = []
        abundanceList = []
        mzResult = []
        abResult = []
        i = 0
        n = 0
        
        while n < len(filtetedList):
            
            isoCount = filtetedList[n].count(':')
            
            while i < isoCount:

                mzResult = filtetedList[n]
                mzResult = mzResult.split(':')
                mzResult = mzResult[i]
                mzResult = mzResult.split('-')
                mzResult = mzResult[0]
                if "+" in mzResult:
                    mzResult = mzResult.split("+")[1]

                abResult = filtetedList[n]
                abResult = abResult.split(':')
                abResult = abResult[i]
                abResult = abResult.split('-')
                abResult = abResult[2]
                
                massList.append(mzResult)
                abundanceList.append(abResult)

                i = i + 1

            i = 0
            n = n + 1

        currentMass = 0
        resNum = 15000
        resNum = 1/float(resNum)*225
        maxCounts = 0
        n = 0

        for each in abundanceList:
            if maxCounts < float(abundanceList[n]):
                maxCounts = float(abundanceList[n])
            n = n + 1
            
        n = 0
        
        for each in abundanceList:
            abundanceList[n] = float(abundanceList[n]) / float(maxCounts) * 100
            n = n + 1
            
        intNum = 0
        n = 0
        maxCounts = 100
        
        maxMass = 0
        minMass = 1000000000
        
        resVal = StringVar()
        resVal = 15000
        
        labelHeight = 0
        primary.ax2.clear()
        colorNum = 0.2
        colorChange = 0

        intNum = 0
        
        while intNum < len(massList):
            if float(massList[intNum]) > float(maxMass):
                maxMass = float(massList[intNum])  + 2
            if float(massList[intNum]) < float(minMass):
                minMass = float(massList[intNum])  - 1
                
            intNum = intNum + 1

        labelHeight = (100+100/4) * 0.05 #was 0.14
        intNum = 0
        colorsMap = [(0.976,0.333,0.518), (0.976,0.333,0.518), (0.976,0.333,0.518)]
        
        while intNum < len(abundanceList):
          
            primary.ax2.plot([float(massList[intNum]) - (150/float(resVal)),float(massList[intNum])], [0,(float(abundanceList[intNum]))], color = (colorNum,1-colorNum,0.952)) #"b")
            primary.ax2.plot([float(massList[intNum]) + (150/float(resVal)),float(massList[intNum])], [0,(float(abundanceList[intNum]))], color = (colorNum,1-colorNum,0.952)) #"b")
            primary.ax2.plot([0,30000], [0,0], "b", linewidth=0.5)
            primary.ax2.text(float(massList[intNum]), (float(abundanceList[intNum]))+labelHeight, str(format(float(massList[intNum]),'.4f')), fontsize=9, rotation=80)

            primary.ax2.set_xlabel('Mass to charge (m/z)')
            primary.ax2.set_title('Isotope Pattern')
            primary.ax2.set_ylabel('Relative Abundance')

            if colorChange == 0:
                colorNum = colorNum + 0.02

            if colorChange == 1:
                colorNum = colorNum - 0.02
            
            if colorNum > 1:
                colorNum = colorNum - 0.04
                colorChange = 1

            if colorNum < 0.2:
                colorNum = colorNum + 0.04
                colorChange = 0

            intNum = intNum + 1

        primary.ax2.set_ylim( ((-(100+100/4))/50,maxCounts+maxCounts/4) )
        primary.ax2.set_xlim( (minMass - ((maxMass-minMass)*0.1), maxMass + ((maxMass-minMass)*0.1)) )

        if currentMode == "Molecular":
            primary.ax2.text(maxMass - ((maxMass-minMass)*0.21), 115, "Hit rate: " + str(selectedRate) + "%", fontsize=11) #, rotation=80)
        primary.canvas.draw()
        
        return

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('DCAnalysis 1.10')
    img = PhotoImage(data=iconData)
    app.tk.call('wm', 'iconphoto', app._w, img)
    app.mainloop()

