# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 266_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 581 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_stmts ::= _stmts . stmt
_stmts ::= _stmts stmt . 
_stmts ::= stmt . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
break ::= POP_BLOCK . BREAK_LOOP
break ::= POP_BLOCK . POP_TOP BREAK_LOOP
break ::= POP_TOP . BREAK_LOOP
call ::= expr . CALL_METHOD_0
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg CALL_METHOD_1
call ::= expr CALL_METHOD_0 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . CALL_METHOD_1
call ::= expr pos_arg CALL_FUNCTION_1 . 
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr LOAD_CONST CALL_FUNCTION_KW_1 . 
call_stmt ::= call . 
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
compare_chained ::= expr . compared_chained_middle ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compared_chained_middle ROT_TWO POP_TOP _come_froms
compare_chained37 ::= expr . compared_chained_middlea_37
compare_chained37 ::= expr . compared_chained_middlec_37
compare_chained37_false ::= expr . compare_chained_right_false_37
compare_chained37_false ::= expr . compared_chained_middle_false_37
compare_chained37_false ::= expr . compared_chained_middleb_false_37
compare_chained_right_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_false_37 POP_TOP JUMP_BACK COME_FROM
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained_right COME_FROM
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compared_chained_middle COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightc_37 POP_TOP JUMP_FORWARD COME_FROM
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 COME_FROM POP_TOP COME_FROM
compared_chained_middleb_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middlec_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 POP_TOP
continues ::= _stmts . lastl_stmt continue
except_cond1 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP POP_EXCEPT
except_cond1 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP POP_EXCEPT
except_cond1 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP POP_TOP POP_TOP POP_EXCEPT
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP POP_TOP POP_TOP POP_EXCEPT
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . POP_TOP POP_TOP POP_EXCEPT
except_cond_as ::= DUP_TOP . expr COMPARE_OP POP_JUMP_IF_FALSE POP_TOP STORE_FAST POP_TOP
except_cond_as ::= DUP_TOP expr . COMPARE_OP POP_JUMP_IF_FALSE POP_TOP STORE_FAST POP_TOP
except_cond_as ::= DUP_TOP expr COMPARE_OP . POP_JUMP_IF_FALSE POP_TOP STORE_FAST POP_TOP
except_cond_as ::= DUP_TOP expr COMPARE_OP POP_JUMP_IF_FALSE . POP_TOP STORE_FAST POP_TOP
except_cond_as ::= DUP_TOP expr COMPARE_OP POP_JUMP_IF_FALSE POP_TOP . STORE_FAST POP_TOP
except_cond_as ::= DUP_TOP expr COMPARE_OP POP_JUMP_IF_FALSE POP_TOP STORE_FAST . POP_TOP
except_cond_as ::= DUP_TOP expr COMPARE_OP POP_JUMP_IF_FALSE POP_TOP STORE_FAST POP_TOP . 
except_handler_as ::= COME_FROM_FINALLY . except_cond_as tryfinallystmt POP_EXCEPT JUMP_FORWARD COME_FROM
except_handler_as ::= COME_FROM_FINALLY except_cond_as . tryfinallystmt POP_EXCEPT JUMP_FORWARD COME_FROM
except_ret38 ::= SETUP_FINALLY . expr ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
except_ret38 ::= SETUP_FINALLY . expr ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
except_ret38 ::= SETUP_FINALLY expr . ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
except_ret38 ::= SETUP_FINALLY expr . ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
except_ret38a ::= COME_FROM_FINALLY . POP_TOP POP_TOP POP_TOP expr ROT_FOUR POP_EXCEPT RETURN_VALUE END_FINALLY
except_return_value ::= expr . POP_BLOCK RETURN_VALUE
except_return_value ::= expr POP_BLOCK . RETURN_VALUE
except_return_value ::= expr POP_BLOCK RETURN_VALUE . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= formatted_value1 . 
expr ::= formatted_value_debug . 
expr ::= joined_str . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
formatted_value1 ::= expr . FORMAT_VALUE
formatted_value1 ::= expr FORMAT_VALUE . 
formatted_value_debug ::= LOAD_STR . formatted_value1 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR . formatted_value2 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR formatted_value1 . BUILD_STRING_2
formatted_value_debug ::= LOAD_STR formatted_value1 BUILD_STRING_2 . 
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
jmp_false ::= POP_JUMP_IF_FALSE . 
joined_str ::= expr . expr BUILD_STRING_2
joined_str ::= expr expr . BUILD_STRING_2
joined_str ::= expr expr BUILD_STRING_2 . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lstmt . 
l_stmts ::= returns . 
lstmt ::= stmt . 
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
pop_return ::= POP_TOP . return_expr RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
popb_return ::= return_expr POP_BLOCK . RETURN_VALUE
popb_return ::= return_expr POP_BLOCK RETURN_VALUE . 
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= popb_return . 
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return_except ::= stmts . POP_BLOCK return
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
returns ::= _stmts return . 
returns ::= return . 
returns_in_except ::= _stmts . except_return_value
returns_in_except ::= _stmts except_return_value . 
sf_pb_call_returns ::= SETUP_FINALLY . POP_BLOCK CALL_FINALLY returns
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts ::= returns . 
suite_stmts_opt ::= suite_stmts . 
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
try_elsestmtl38 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38 COME_FROM else_suitel \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38 COME_FROM else_suitel opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitel \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitel opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitel \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitel opt_come_from_except
try_except ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38
try_except ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38
try_except ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38
try_except38 ::= SETUP_FINALLY . POP_BLOCK POP_TOP \e_suite_stmts_opt except_handler38a
try_except38 ::= SETUP_FINALLY . POP_BLOCK POP_TOP suite_stmts_opt except_handler38a
try_except38 ::= SETUP_FINALLY . POP_BLOCK suite_stmts except_handler38b
try_except38r ::= SETUP_FINALLY . return_except except_handler38b
try_except38r2 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r4 ::= SETUP_FINALLY . returns_in_except COME_FROM_FINALLY except_cond1 return COME_FROM END_FINALLY
try_except38r4 ::= SETUP_FINALLY returns_in_except . COME_FROM_FINALLY except_cond1 return COME_FROM END_FINALLY
try_except38r4 ::= SETUP_FINALLY returns_in_except COME_FROM_FINALLY . except_cond1 return COME_FROM END_FINALLY
try_except_as ::= SETUP_FINALLY . POP_BLOCK suite_stmts except_handler_as END_FINALLY COME_FROM
try_except_as ::= SETUP_FINALLY . suite_stmts except_handler_as END_FINALLY COME_FROM
try_except_as ::= SETUP_FINALLY suite_stmts . except_handler_as END_FINALLY COME_FROM
try_except_ret38 ::= SETUP_FINALLY . returns except_ret38a
try_except_ret38 ::= SETUP_FINALLY returns . except_ret38a
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY suite_stmts
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinally36 ::= SETUP_FINALLY returns . COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally36 ::= SETUP_FINALLY returns . COME_FROM_FINALLY suite_stmts
tryfinally36 ::= SETUP_FINALLY returns . COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinally36 ::= SETUP_FINALLY returns COME_FROM_FINALLY . suite_stmts
tryfinally36 ::= SETUP_FINALLY returns COME_FROM_FINALLY . suite_stmts_opt END_FINALLY
tryfinally36 ::= SETUP_FINALLY returns COME_FROM_FINALLY \e_suite_stmts_opt . END_FINALLY
tryfinally38rstmt3 ::= SETUP_FINALLY . expr POP_BLOCK CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY ss_end_finally
tryfinally38rstmt3 ::= SETUP_FINALLY expr . POP_BLOCK CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY ss_end_finally
tryfinally38stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally_return_stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinally_return_stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinally_return_stmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . LOAD_CONST COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt POP_BLOCK . LOAD_CONST COME_FROM_FINALLY suite_stmts_opt END_FINALLY
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  12        54  POP_BLOCK        
->                56  POP_EXCEPT       
                  58  CALL_FINALLY         64  'to 64'
                  60  LOAD_CONST               None
                  62  RETURN_VALUE     
                64_0  COME_FROM            58  '58'
                64_1  COME_FROM_FINALLY    38  '38'
                  64  LOAD_CONST               None
                  66  STORE_FAST               'e'
                  68  DELETE_FAST              'e'
                  70  END_FINALLY      
                  72  POP_EXCEPT       
                  74  JUMP_FORWARD         78  'to 78'
                76_0  COME_FROM            30  '30'
                  76  END_FINALLY      
import json
from json2xml import json2xml

def convert_json_to_xmlParse error at or near `POP_EXCEPT' instruction at offset 56


json_input = '{"key": "value", "typecode": "unexpected_type"}'
xml_output = convert_json_to_xml(json.loads(json_input))
print(xml_output)
