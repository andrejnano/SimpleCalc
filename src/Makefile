# + ------------------------ +
# | ~ Makefile / SimpleCalc  |
# |                          |
# | ~ 2. projekt IVS / 2017  |
# | ~ FIT VUT, BRNO          |
# |                          |
# | ~ Peter Marko            |
# | ~ Stanislav Mechl        |
# | ~ Andrej Nano            |
# + ------------------------ +   

.PHONY: all doc clean

PROGRAM_NAME='main.py'
MAT_MODULE_NAME='mat_module.py'

doc: Doxyfile ${PROGRAM_NAME} ${MAT_MODULE_NAME} 
	doxygen Doxyfile
	cd doc && make

clean:
	 cd doc && find . -type f -not -name 'refman.pdf' -print0 | xargs -0 rm --  | rm -f && cd .. && rm -rf ./__pycache__

run:
	python ./main.py

