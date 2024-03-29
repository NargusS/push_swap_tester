# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: achane-l <achane-l@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/10/20 14:16:36 by achane-l          #+#    #+#              #
#    Updated: 2021/10/24 19:27:23 by achane-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NUMBER_OF_TESTS = 1000
SIZE_OF_STACK = 100
MIN_VALUE = -1000
MAX_VALUE = 1000
RANDOM = "yes"
DIR = ../../Push_Swap
NOTES = \xF0\x9F\x93\x9D
BALEINE = \xF0\x9F\x90\x8B
ROCKET = \xF0\x9F\x9A\x80

.PHONY: push_swap fclean

all: push_swap
	@echo "Lancement des tests ${BALEINE} ${NOTES}"
	@python3 main.py ${NUMBER_OF_TESTS} ${SIZE_OF_STACK} ${MIN_VALUE} ${MAX_VALUE} ${RANDOM}
push_swap:
	@cd ../ && $(MAKE) -s
	@printf "COMPILATION DONE\\360\237\246\204\n"
clean:
	@rm -rf __pycache__
	@sh errors/erase_file_error.sh
fclean: clean
	@cd ../ && $(MAKE) -s fclean
	@echo "Merci d'avoir utiliser mon testeur que du love ${BALEINE} ${NOTES}"
re:	fclean all