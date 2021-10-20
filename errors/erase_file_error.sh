# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    erase_file_error.sh                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: achane-l <achane-l@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/10/20 14:16:40 by achane-l          #+#    #+#              #
#    Updated: 2021/10/20 14:29:21 by achane-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!bin/bash

if [ -f errors/command_test_* ]
then
    rm errors/command_test_*
fi
if [ -f errors/stacks_of_test_* ]
then
    rm errors/stacks_of_test_*
fi