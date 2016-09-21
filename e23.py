#!/usr/bin/python
#-*- coding: utf-8 -*-


import sys

my_input = input if sys.version_info >= (3,0) else raw_input

if __name__ == "__main__":
	q1 = {'l':None, 'r':None, 'q':"서비스센터에 의뢰하라."}
	q2 = {'l':None, 'r':None, 'q':"초크가 제대로 여닫히는지 확인하라."}
	q3 = {'l':q2, 'r':q1, 'q':"차에 연료 분사 장치가 있는가?"}
	q4 = {'l':q3, 'r':None, 'q':"엔진이 동작한 후 바로 꺼지는가?"}
	q5 = {'l':None, 'r':None, 'q':"점화 플러그 연결 상태를 점검하라"}
	q6 = {'l': q5, 'r': q4, 'q':"시동이 완전히 걸리지 않는가?"}
	q7 = {'l':None, 'r':None, 'q':"배터리를 교체하고 다시 시도하라"}
	q8 = {'l':None, 'r':None, 'q':"케이블을 교체하고 다시 시도하라"}
	q9 = {'l':None, 'r':None, 'q':"단자를 깨끗이하고 다시 시도하라"}
	q10 = {'l': q7, 'r': q6, 'q':"차에서 달깍거리는 소리가 나는가?"}
	q11 = {'l': q9, 'r': q8, 'q':"배터리 단자가 부식되었는가?"}
	root = {'l': q11, 'r': q10, 'q':"열쇠를 꽂고 돌렸을 때 차가 조용한가?"}
	
	current_node = root
	while True:
		if current_node['l'] == None and current_node['r'] == None:
			print(current_node['q'])
			break
		while True:
			a = my_input(current_node['q'])
			if current_node['l'] != None and a == "y":
				current_node = current_node['l']
				break
			elif current_node['r'] != None and a == "n":
				current_node = current_node['r']
				break

