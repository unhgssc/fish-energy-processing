SPECIAL>NOINTERACTION
SPECIAL>LOADMODEL|"E:\fish-energy-tradeoff-vensim\energy-fish-cost tradeoffs-042819.vmf"


SIMULATE>SETVAL|dam1 install Pool and Weir=${field1}
SIMULATE>SETVAL|dam1 install Denil=${field2}
SIMULATE>SETVAL|dam1 install Fish Lift=${field3}
SIMULATE>SETVAL|remove dam1=${field4}

SIMULATE>SETVAL|dam2 install Pool and Weir=${field5}
SIMULATE>SETVAL|dam2 install Denil=${field6}
SIMULATE>SETVAL|dam2 install Fish Lift=${field7}
SIMULATE>SETVAL|remove dam2=${field8}

SIMULATE>SETVAL|dam3 install Pool and Weir=${field9}
SIMULATE>SETVAL|dam3 install Denil=${field10}
SIMULATE>SETVAL|dam3 install Fish Lift=${field11}
SIMULATE>SETVAL|remove dam3=${field12}

SIMULATE>SETVAL|dam4 install Pool and Weir=${field13}
SIMULATE>SETVAL|dam4 install Denil=${field14}
SIMULATE>SETVAL|dam4 install Fish Lift=${field15}
SIMULATE>SETVAL|remove dam4=${field16}

SIMULATE>SETVAL|dam5 install Pool and Weir=${field17}
SIMULATE>SETVAL|dam5 install Denil=${field18}
SIMULATE>SETVAL|dam5 install Fish Lift=${field19}
SIMULATE>SETVAL|remove dam5=${field20}


SIMULATE>RUNNAME|fish-energy-run-${RunNumber}
MENU>RUN|0
MENU>VDF2CSV|fish-energy-run-${RunNumber}.vdf|results_csv/fish-energy-run-${RunNumber}.csv|fish-energy-run-variables.list


MENU>EXIT
