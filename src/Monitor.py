# -*- generated by 1.0.12 -*-
import da
PatternExpr_323 = da.pat.TuplePattern([da.pat.ConstantPattern('init_files')])
PatternExpr_401 = da.pat.TuplePattern([da.pat.ConstantPattern('init_params'), da.pat.FreePattern('n_users'), da.pat.FreePattern('n_traitors'), da.pat.FreePattern('stake_traitors'), da.pat.FreePattern('tau_step'), da.pat.FreePattern('block_size')])
PatternExpr_456 = da.pat.TuplePattern([da.pat.ConstantPattern('correctness'), da.pat.FreePattern('agr'), da.pat.FreePattern('val'), da.pat.FreePattern('liv'), da.pat.FreePattern('final')])
PatternExpr_505 = da.pat.TuplePattern([da.pat.ConstantPattern('performance'), da.pat.FreePattern('agr'), da.pat.FreePattern('val'), da.pat.FreePattern('liv'), da.pat.FreePattern('time')])
PatternExpr_592 = da.pat.TuplePattern([da.pat.ConstantPattern('flush')])
PatternExpr_794 = da.pat.TuplePattern([da.pat.ConstantPattern('plot')])
PatternExpr_872 = da.pat.TuplePattern([da.pat.ConstantPattern('done')])
PatternExpr_877 = da.pat.BoundPattern('_BoundPattern879_')
PatternExpr_880 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern886_')]), da.pat.TuplePattern([da.pat.ConstantPattern('done')])])
PatternExpr_1131 = da.pat.TuplePattern([da.pat.ConstantPattern('done')])
PatternExpr_1136 = da.pat.BoundPattern('_BoundPattern1137_')
PatternExpr_1138 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern1144_')]), da.pat.TuplePattern([da.pat.ConstantPattern('done')])])
_config_object = {}
from controller import Controller
from algorand import User, create_gossip_neighbours, initial_context
from parameters import Parameters
import csv
import numpy as np
import time
from copy import deepcopy
import json

class Monitor(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._MonitorReceivedEvent_6 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_MonitorReceivedEvent_0', PatternExpr_323, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Monitor_handler_322]), da.pat.EventPattern(da.pat.ReceivedEvent, '_MonitorReceivedEvent_1', PatternExpr_401, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Monitor_handler_400]), da.pat.EventPattern(da.pat.ReceivedEvent, '_MonitorReceivedEvent_2', PatternExpr_456, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Monitor_handler_455]), da.pat.EventPattern(da.pat.ReceivedEvent, '_MonitorReceivedEvent_3', PatternExpr_505, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Monitor_handler_504]), da.pat.EventPattern(da.pat.ReceivedEvent, '_MonitorReceivedEvent_4', PatternExpr_592, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Monitor_handler_591]), da.pat.EventPattern(da.pat.ReceivedEvent, '_MonitorReceivedEvent_5', PatternExpr_794, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Monitor_handler_793]), da.pat.EventPattern(da.pat.ReceivedEvent, '_MonitorReceivedEvent_6', PatternExpr_872, sources=[PatternExpr_877], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, **rest_1173):
        super().setup(**rest_1173)
        self._state.storage = [True, True, True]
        self._state.number = 0
        self._state.final = True
        self._state.times = []
        self._state.n_users = None
        self._state.n_traitors = None
        self._state.stake_traitors = None
        self._state.tau_step = None
        self._state.lambda_block = None
        self._state.lambda_step = None
        self._state.c_file = None
        self._state.c_csvwriter = None
        self._state.p_file = None
        self._state.p_csvwriter = None
        self._state.block_size = None
        self._state.labels = [['Number of Users ', 'Number of Users vs Latency'], ['% Malicious Users', ' % Malicious Users vs Latency'], ['% Stake of Malicious Users', '% Stake of Malicious Users vs Latency'], ['Committee Size', 'Committee Size vs Latency'], ['Block Size (KB)', 'Block Size vs Latency']]
        self._state.plot_file = open('temp.json', 'w')
        self._state.plot_data = [[], []]

    def run(self):
        super()._label('_st_label_869', block=False)
        _st_label_869 = 0
        while (_st_label_869 == 0):
            _st_label_869 += 1
            if PatternExpr_880.match_iter(self._MonitorReceivedEvent_6, _BoundPattern886_=self.parent(), SELF_ID=self._id):
                _st_label_869 += 1
            else:
                super()._label('_st_label_869', block=True)
                _st_label_869 -= 1

    def get_xaxis(self):
        switcher = {0: self._state.n_users, 1: ((self._state.n_traitors * 100.0) / self._state.n_users), 2: (self._state.stake_traitors * 100), 3: self._state.tau_step, 4: self._state.block_size}
        return switcher[self._state.number]

    def _Monitor_handler_322(self):
        self._state.p_file = open('performance.csv', 'w')
        self._state.p_csvwriter = csv.writer(self._state.p_file, lineterminator='\n')
        self._state.p_csvwriter.writerow(['NumUsers', 'NumTraitors', 'BlockSize', 'CommitteeSize', 'TraitorStake', 'Consensus', 'Agreement', 'Validity', 'Liveness', 'Time'])
        self._state.c_file = open('correctness.csv', 'w')
        self._state.c_csvwriter = csv.writer(self._state.c_file, lineterminator='\n')
        self._state.c_csvwriter.writerow(['NumUsers', 'NumTraitors', 'TraitorStake', 'CommitteeSize', 'BlockSize', 'Consensus', 'Agreement', 'Validity', 'Liveness'])
    _Monitor_handler_322._labels = None
    _Monitor_handler_322._notlabels = None

    def _Monitor_handler_400(self, n_users, n_traitors, stake_traitors, tau_step, block_size):
        self._state.n_users = n_users
        self._state.n_traitors = n_traitors
        self._state.stake_traitors = stake_traitors
        self._state.tau_step = tau_step
        self._state.block_size = block_size
        self._state.storage = [True, True, True]
        self._state.times = []
    _Monitor_handler_400._labels = None
    _Monitor_handler_400._notlabels = None

    def _Monitor_handler_455(self, agr, val, liv, final):
        (oldagr, oldval, oldliv) = self._state.storage
        self._state.final = (self._state.final and final)
        self._state.storage = [(agr and oldagr), (val and oldval), (liv and oldliv)]
    _Monitor_handler_455._labels = None
    _Monitor_handler_455._notlabels = None

    def _Monitor_handler_504(self, agr, val, liv, time):
        (oldagr, oldval, oldliv) = self._state.storage
        self._state.times.append(time)
        self._state.storage = [(agr and oldagr), (val and oldval), (liv and oldliv)]
    _Monitor_handler_504._labels = None
    _Monitor_handler_504._notlabels = None

    def _Monitor_handler_591(self):
        consensus = ('Final' if self._state.final else 'Tentative')
        self._state.c_csvwriter.writerow(([self._state.n_users, ((self._state.n_traitors * 100.0) / self._state.n_users), (self._state.stake_traitors * 100), self._state.tau_step, self._state.block_size, consensus] + self._state.storage))
        self._state.c_file.flush()
        print((([self._state.n_users, ((self._state.n_traitors * 100.0) / self._state.n_users), self._state.block_size, self._state.tau_step, self._state.block_size, (self._state.stake_traitors * 100), consensus] + self._state.storage) + [round(((sum(self._state.times) * 1.0) / len(self._state.times)), 4)]))
        self._state.p_csvwriter.writerow((([self._state.n_users, ((self._state.n_traitors * 100.0) / self._state.n_users), self._state.block_size, self._state.tau_step, self._state.block_size, (self._state.stake_traitors * 100), consensus] + self._state.storage) + [round(((sum(self._state.times) * 1.0) / len(self._state.times)), 4)]))
        self._state.p_file.flush()
        self._state.plot_data[0].append(self.get_xaxis())
        self._state.plot_data[1].append(round(((sum(self._state.times) * 1.0) / len(self._state.times)), 4))
    _Monitor_handler_591._labels = None
    _Monitor_handler_591._notlabels = None

    def _Monitor_handler_793(self):
        obj = {'x': self._state.plot_data[0], 'y': self._state.plot_data[1], 'xlabel': self._state.labels[self._state.number][0], 'ylabel': 'Latency (s)', 'title': self._state.labels[self._state.number][1]}
        self._state.plot_file.write((json.dumps(obj) + '\n'))
        self._state.plot_file.flush()
        self._state.number += 1
        self._state.plot_data = [[], []]
    _Monitor_handler_793._labels = None
    _Monitor_handler_793._notlabels = None

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._Node_ReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_Node_ReceivedEvent_0', PatternExpr_1131, sources=[PatternExpr_1136], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def run(self):
        params = Parameters()
        monitor = self.new(Monitor, ())
        self._start(monitor)
        self.send(('init_files',), to=monitor)
        template = [30, 5, 0.25, 10, 0]
        n_users_vals = range(20, 51, 5)
        n_traitors_vals = range(0, 17, 4)
        traitor_stake_vals = [float(x) for x in np.concatenate([np.arange(0, 0.33, 0.06), np.array([0.33, 0.34])])]
        tau_step_vals = range(5, 21, 5)
        block_size_vals = [float(x) for x in np.linspace(0, 3, 7)]
        value_lists = [n_users_vals, n_traitors_vals, traitor_stake_vals, tau_step_vals, block_size_vals]
        for i in range(5):
            values = deepcopy(template)
            for val in value_lists[i]:
                values[i] = val
                for _ in range(3):
                    (n_users, n_traitors, traitor_stake, params.tau_step, block_size) = values
                    params.tau_final = params.tau_step
                    self.output(n_users, n_traitors, traitor_stake, params.tau_step, block_size)
                    self.send(('init_params', n_users, n_traitors, traitor_stake, params.tau_step, block_size), to=monitor)
                    context = initial_context()
                    ps = self.new(User, num=n_users)
                    ctrl = self.new(Controller, (ps, params, context, n_traitors, traitor_stake, False, True, monitor, block_size))
                    users_list = list(ps)
                    for p in ps:
                        neighbours_set = create_gossip_neighbours(users_list, p)
                        self._setup(p, (neighbours_set, params, ctrl, context, True, block_size))
                    self._start(ps)
                    self._start(ctrl)
                    super()._label('_st_label_1128', block=False)
                    _st_label_1128 = 0
                    while (_st_label_1128 == 0):
                        _st_label_1128 += 1
                        if PatternExpr_1138.match_iter(self._Node_ReceivedEvent_0, _BoundPattern1144_=ctrl):
                            _st_label_1128 += 1
                        else:
                            super()._label('_st_label_1128', block=True)
                            _st_label_1128 -= 1
                    else:
                        if (_st_label_1128 != 2):
                            continue
                    if (_st_label_1128 != 2):
                        break
                self.send(('flush',), to=monitor)
                time.sleep(1)
            self.send(('plot',), to=monitor)
            time.sleep(1)
        self.send(('done',), to=monitor)