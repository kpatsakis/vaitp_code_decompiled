# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 311_4.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1576 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_stmts ::= _stmts . stmt
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
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
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
call ::= expr . CALL_METHOD_0
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_METHOD_2
call ::= expr CALL_METHOD_0 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_METHOD_2
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_METHOD_2
call ::= expr pos_arg pos_arg CALL_METHOD_2 . 
call_stmt ::= call . 
call_stmt ::= expr . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
compare ::= compare_single . 
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
compare_single ::= expr expr COMPARE_OP . 
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained_right COME_FROM
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compared_chained_middle COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightc_37 POP_TOP JUMP_FORWARD COME_FROM
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 COME_FROM POP_TOP COME_FROM
compared_chained_middleb_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middlec_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 POP_TOP
continues ::= _stmts . lastl_stmt continue
except_ret38 ::= SETUP_FINALLY . expr ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
except_ret38 ::= SETUP_FINALLY . expr ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
except_ret38 ::= SETUP_FINALLY expr . ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
except_ret38 ::= SETUP_FINALLY expr . ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
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
import ::= LOAD_CONST . LOAD_CONST alias
import_as37 ::= LOAD_CONST . LOAD_CONST importlist37 store POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST importlist POP_TOP
import_from37 ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP
import_from_as37 ::= LOAD_CONST . LOAD_CONST import_from_attr37 store POP_TOP
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR IMPORT_STAR
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
lc_setup_finally ::= LOAD_CONST . SETUP_FINALLY
lstmt ::= stmt . 
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
popb_return ::= return_expr POP_BLOCK . RETURN_VALUE
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
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
returns_in_except ::= _stmts . except_return_value
sf_pb_call_returns ::= SETUP_FINALLY . POP_BLOCK CALL_FINALLY returns
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= call_stmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
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
try_except_as ::= SETUP_FINALLY . POP_BLOCK suite_stmts except_handler_as END_FINALLY COME_FROM
try_except_as ::= SETUP_FINALLY . suite_stmts except_handler_as END_FINALLY COME_FROM
try_except_as ::= SETUP_FINALLY suite_stmts . except_handler_as END_FINALLY COME_FROM
try_except_ret38 ::= SETUP_FINALLY . returns except_ret38a
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY suite_stmts
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP \e_suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP \e_suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP suite_stmts_opt END_FINALLY POP_TOP
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
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH . store \e_suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH . store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr SETUP_WITH . store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH . store suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH . store suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH . store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr SETUP_WITH . store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store . suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store . suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr SETUP_WITH store . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store \e_suite_stmts_opt . COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr SETUP_WITH store \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store suite_stmts . POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store suite_stmts_opt . COME_FROM_WITH with_suffix
with_as ::= expr SETUP_WITH store suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH
with_as ::= expr SETUP_WITH store suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as_pass ::= expr . SETUP_WITH store \e_pass POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as_pass ::= expr . SETUP_WITH store pass POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as_pass ::= expr SETUP_WITH . store \e_pass POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as_pass ::= expr SETUP_WITH . store pass POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as_pass ::= expr SETUP_WITH store . pass POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with_as_pass ::= expr SETUP_WITH store \e_pass . POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  10        16  LOAD_GLOBAL              len
                  18  LOAD_FAST                'archive'
                  20  LOAD_METHOD              namelist
                  22  CALL_METHOD_0         0  '0 positional arguments'
                  24  CALL_FUNCTION_1       1  '1 positional argument'
                  26  LOAD_CONST               1
                  28  COMPARE_OP               >
                  30  POP_BLOCK        
->                32  ROT_TWO          
                  34  BEGIN_FINALLY    
                  36  WITH_CLEANUP_START
                  38  WITH_CLEANUP_FINISH
                  40  POP_FINALLY           0  ''
                  42  POP_BLOCK        
                  44  RETURN_VALUE     
                46_0  COME_FROM_WITH       12  '12'
                  46  WITH_CLEANUP_START
                  48  WITH_CLEANUP_FINISH
                  50  END_FINALLY      
                  52  POP_BLOCK        
                  54  JUMP_FORWARD         78  'to 78'
                56_0  COME_FROM_FINALLY     0  '0'
import os, zipfile
from thefuck.utils import for_app
from thefuck.shells import shell

def _is_bad_zipParse error at or near `ROT_TWO' instruction at offset 32


def _zip_file(command):
    for c in command.script_parts[1[:None]]:
        if not c.startswith("-"):
            if c.endswith(".zip"):
                return c
            return "{}.zip".format(c)


@for_app("unzip")
def match(command):
    if "-d" in command.script:
        return False
    zip_file = _zip_file(command)
    if zip_file:
        return _is_bad_zip(zip_file)
    return False


def get_new_command(command):
    return "{} -d {}".formatcommand.scriptshell.quote(_zip_file(command)[None[:-4]])


def side_effect(old_cmd, command):
    with zipfile.ZipFile_zip_file(old_cmd)"r" as archive:
        for file in archive.namelist:
            if not os.path.abspath(file).startswith(os.getcwd):
                pass
            else:
                try:
                    os.remove(file)
                except OSError:
                    pass


requires_output = False
