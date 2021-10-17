NUMBER_OF_TESTS = 10
SIZE_OF_STACK = 100
DIR = ../../Push_Swap
NOTES = '\xF0\x9F\x93\x9D'
BALEINE = '\xF0\x9F\x90\x8B'

.PHONY: push_swap fclean

all: push_swap
	@echo -e 'Lancement des tests' ${BALEINE} ${NOTES}
	@python3 main.py ${NUMBER_OF_TESTS} ${SIZE_OF_STACK}
push_swap:
	@$(MAKE) -C $(DIR)
	@printf "COMPILATION DONE\\360\237\246\204\n"
clean:
	@rm -rf __pycache__
fclean: clean
	@$(MAKE) -C $(DIR) fclean
re:	all fclean