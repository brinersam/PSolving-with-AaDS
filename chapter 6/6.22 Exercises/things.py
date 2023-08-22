import turtle as tut
import math
import operator as ops

class BinaryMinHeap():
    def __init__(self, heap=None):
        if heap is None:
            self.heap = []
        else:
            self.heap = heap
            self.heapify()

    def insert(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)

    def bubble_up(self, index):
        while self.heap[index] < self.heap[(index - 1) // 2] and index > 0:
            self.heap[index], self.heap[(index - 1) // 2] = self.heap[(index - 1) // 2], self.heap[index]
            index = (index - 1) // 2

    def bubble_down(self, index):
        while True:
            minchild_idx = self.get_min_child_idx(index)
            if minchild_idx is None:
                break

            if self.heap[minchild_idx] > self.heap[index]:
                break

            self.heap[index], self.heap[minchild_idx] = self.heap[minchild_idx], self.heap[index]
            index = minchild_idx

    def get_min_child_idx(self, index):
        left_idx = index * 2 + 1
        right_idx = index * 2 + 2
        max_idx = len(self.heap) - 1
        if left_idx > max_idx:  # if left does not exist, right doesnt exist either
            return None
        assert left_idx <= max_idx  # left exists
        if right_idx > max_idx:  # if right doesnt exist, but left exists, return left
            return left_idx
        if self.heap[left_idx] > self.heap[right_idx]:
            return right_idx
        else:
            return left_idx

    def peek(self):
        return self.heap[0]

    def heapify(self,notheap = None):
        if notheap is None:
            self.heap = self.heap[:]  # [:] to avoid pointing at the list
        else:
            self.heap = notheap[:]
        i = len(self.heap) // 2 - 1
        while i >= 0:
            self.bubble_down(i)
            i -= 1

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        oldmin = self.heap.pop()
        self.bubble_down(0)
        return oldmin

class HeapDrawer():
    def __init__(self, heap, turtle=None):
        self.turtle = turtle
        if turtle is None:
            self.turtle = tut.Turtle()
        self.heap = heap.heap

        # baked the coordinates
        self.coordinates = [(0.0, 240), (-450.0, 180), (450.0, 180), (-675.0, 120), (-225.0, 120), (225.0, 120),
                            (675.0, 120), (-787.5, 60), (-562.5, 60), (-337.5, 60), (-112.5, 60), (112.5, 60),
                            (337.5, 60), (562.5, 60), (787.5, 60), (-843.75, 0), (-731.25, 0), (-618.75, 0),
                            (-506.25, 0), (-393.75, 0), (-281.25, 0), (-168.75, 0), (-56.25, 0), (56.25, 0),
                            (168.75, 0), (281.25, 0), (393.75, 0), (506.25, 0), (618.75, 0), (731.25, 0), (843.75, 0),
                            (-871.875, -60), (-815.625, -60), (-759.375, -60), (-703.125, -60), (-646.875, -60),
                            (-590.625, -60), (-534.375, -60), (-478.125, -60), (-421.875, -60), (-365.625, -60),
                            (-309.375, -60), (-253.125, -60), (-196.875, -60), (-140.625, -60), (-84.375, -60),
                            (-28.125, -60), (28.125, -60), (84.375, -60), (140.625, -60), (196.875, -60),
                            (253.125, -60), (309.375, -60), (365.625, -60), (421.875, -60), (478.125, -60),
                            (534.375, -60), (590.625, -60), (646.875, -60), (703.125, -60), (759.375, -60),
                            (815.625, -60), (871.875, -60), (-885.9375, -120), (-857.8125, -120), (-829.6875, -120),
                            (-801.5625, -120), (-773.4375, -120), (-745.3125, -120), (-717.1875, -120),
                            (-689.0625, -120), (-660.9375, -120), (-632.8125, -120), (-604.6875, -120),
                            (-576.5625, -120), (-548.4375, -120), (-520.3125, -120), (-492.1875, -120),
                            (-464.0625, -120), (-435.9375, -120), (-407.8125, -120), (-379.6875, -120),
                            (-351.5625, -120), (-323.4375, -120), (-295.3125, -120), (-267.1875, -120),
                            (-239.0625, -120), (-210.9375, -120), (-182.8125, -120), (-154.6875, -120),
                            (-126.5625, -120), (-98.4375, -120), (-70.3125, -120), (-42.1875, -120), (-14.0625, -120),
                            (14.0625, -120), (42.1875, -120), (70.3125, -120), (98.4375, -120), (126.5625, -120),
                            (154.6875, -120), (182.8125, -120), (210.9375, -120), (239.0625, -120), (267.1875, -120),
                            (295.3125, -120), (323.4375, -120), (351.5625, -120), (379.6875, -120), (407.8125, -120),
                            (435.9375, -120), (464.0625, -120), (492.1875, -120), (520.3125, -120), (548.4375, -120),
                            (576.5625, -120), (604.6875, -120), (632.8125, -120), (660.9375, -120), (689.0625, -120),
                            (717.1875, -120), (745.3125, -120), (773.4375, -120), (801.5625, -120), (829.6875, -120),
                            (857.8125, -120), (885.9375, -120), (-892.96875, -180), (-878.90625, -180),
                            (-864.84375, -180), (-850.78125, -180), (-836.71875, -180), (-822.65625, -180),
                            (-808.59375, -180), (-794.53125, -180), (-780.46875, -180), (-766.40625, -180),
                            (-752.34375, -180), (-738.28125, -180), (-724.21875, -180), (-710.15625, -180),
                            (-696.09375, -180), (-682.03125, -180), (-667.96875, -180), (-653.90625, -180),
                            (-639.84375, -180), (-625.78125, -180), (-611.71875, -180), (-597.65625, -180),
                            (-583.59375, -180), (-569.53125, -180), (-555.46875, -180), (-541.40625, -180),
                            (-527.34375, -180), (-513.28125, -180), (-499.21875, -180), (-485.15625, -180),
                            (-471.09375, -180), (-457.03125, -180), (-442.96875, -180), (-428.90625, -180),
                            (-414.84375, -180), (-400.78125, -180), (-386.71875, -180), (-372.65625, -180),
                            (-358.59375, -180), (-344.53125, -180), (-330.46875, -180), (-316.40625, -180),
                            (-302.34375, -180), (-288.28125, -180), (-274.21875, -180), (-260.15625, -180),
                            (-246.09375, -180), (-232.03125, -180), (-217.96875, -180), (-203.90625, -180),
                            (-189.84375, -180), (-175.78125, -180), (-161.71875, -180), (-147.65625, -180),
                            (-133.59375, -180), (-119.53125, -180), (-105.46875, -180), (-91.40625, -180),
                            (-77.34375, -180), (-63.28125, -180), (-49.21875, -180), (-35.15625, -180),
                            (-21.09375, -180), (-7.03125, -180), (7.03125, -180), (21.09375, -180), (35.15625, -180),
                            (49.21875, -180), (63.28125, -180), (77.34375, -180), (91.40625, -180), (105.46875, -180),
                            (119.53125, -180), (133.59375, -180), (147.65625, -180), (161.71875, -180),
                            (175.78125, -180), (189.84375, -180), (203.90625, -180), (217.96875, -180),
                            (232.03125, -180), (246.09375, -180), (260.15625, -180), (274.21875, -180),
                            (288.28125, -180), (302.34375, -180), (316.40625, -180), (330.46875, -180),
                            (344.53125, -180), (358.59375, -180), (372.65625, -180), (386.71875, -180),
                            (400.78125, -180), (414.84375, -180), (428.90625, -180), (442.96875, -180),
                            (457.03125, -180), (471.09375, -180), (485.15625, -180), (499.21875, -180),
                            (513.28125, -180), (527.34375, -180), (541.40625, -180), (555.46875, -180),
                            (569.53125, -180), (583.59375, -180), (597.65625, -180), (611.71875, -180),
                            (625.78125, -180), (639.84375, -180), (653.90625, -180), (667.96875, -180),
                            (682.03125, -180), (696.09375, -180), (710.15625, -180), (724.21875, -180),
                            (738.28125, -180), (752.34375, -180), (766.40625, -180), (780.46875, -180),
                            (794.53125, -180), (808.59375, -180), (822.65625, -180), (836.71875, -180),
                            (850.78125, -180), (864.84375, -180), (878.90625, -180), (892.96875, -180),
                            (-896.484375, -240), (-889.453125, -240), (-882.421875, -240), (-875.390625, -240),
                            (-868.359375, -240), (-861.328125, -240), (-854.296875, -240), (-847.265625, -240),
                            (-840.234375, -240), (-833.203125, -240), (-826.171875, -240), (-819.140625, -240),
                            (-812.109375, -240), (-805.078125, -240), (-798.046875, -240), (-791.015625, -240),
                            (-783.984375, -240), (-776.953125, -240), (-769.921875, -240), (-762.890625, -240),
                            (-755.859375, -240), (-748.828125, -240), (-741.796875, -240), (-734.765625, -240),
                            (-727.734375, -240), (-720.703125, -240), (-713.671875, -240), (-706.640625, -240),
                            (-699.609375, -240), (-692.578125, -240), (-685.546875, -240), (-678.515625, -240),
                            (-671.484375, -240), (-664.453125, -240), (-657.421875, -240), (-650.390625, -240),
                            (-643.359375, -240), (-636.328125, -240), (-629.296875, -240), (-622.265625, -240),
                            (-615.234375, -240), (-608.203125, -240), (-601.171875, -240), (-594.140625, -240),
                            (-587.109375, -240), (-580.078125, -240), (-573.046875, -240), (-566.015625, -240),
                            (-558.984375, -240), (-551.953125, -240), (-544.921875, -240), (-537.890625, -240),
                            (-530.859375, -240), (-523.828125, -240), (-516.796875, -240), (-509.765625, -240),
                            (-502.734375, -240), (-495.703125, -240), (-488.671875, -240), (-481.640625, -240),
                            (-474.609375, -240), (-467.578125, -240), (-460.546875, -240), (-453.515625, -240),
                            (-446.484375, -240), (-439.453125, -240), (-432.421875, -240), (-425.390625, -240),
                            (-418.359375, -240), (-411.328125, -240), (-404.296875, -240), (-397.265625, -240),
                            (-390.234375, -240), (-383.203125, -240), (-376.171875, -240), (-369.140625, -240),
                            (-362.109375, -240), (-355.078125, -240), (-348.046875, -240), (-341.015625, -240),
                            (-333.984375, -240), (-326.953125, -240), (-319.921875, -240), (-312.890625, -240),
                            (-305.859375, -240), (-298.828125, -240), (-291.796875, -240), (-284.765625, -240),
                            (-277.734375, -240), (-270.703125, -240), (-263.671875, -240), (-256.640625, -240),
                            (-249.609375, -240), (-242.578125, -240), (-235.546875, -240), (-228.515625, -240),
                            (-221.484375, -240), (-214.453125, -240), (-207.421875, -240), (-200.390625, -240),
                            (-193.359375, -240), (-186.328125, -240), (-179.296875, -240), (-172.265625, -240),
                            (-165.234375, -240), (-158.203125, -240), (-151.171875, -240), (-144.140625, -240),
                            (-137.109375, -240), (-130.078125, -240), (-123.046875, -240), (-116.015625, -240),
                            (-108.984375, -240), (-101.953125, -240), (-94.921875, -240), (-87.890625, -240),
                            (-80.859375, -240), (-73.828125, -240), (-66.796875, -240), (-59.765625, -240),
                            (-52.734375, -240), (-45.703125, -240), (-38.671875, -240), (-31.640625, -240),
                            (-24.609375, -240), (-17.578125, -240), (-10.546875, -240), (-3.515625, -240),
                            (3.515625, -240), (10.546875, -240), (17.578125, -240), (24.609375, -240),
                            (31.640625, -240), (38.671875, -240), (45.703125, -240), (52.734375, -240),
                            (59.765625, -240), (66.796875, -240), (73.828125, -240), (80.859375, -240),
                            (87.890625, -240), (94.921875, -240), (101.953125, -240), (108.984375, -240),
                            (116.015625, -240), (123.046875, -240), (130.078125, -240), (137.109375, -240),
                            (144.140625, -240), (151.171875, -240), (158.203125, -240), (165.234375, -240),
                            (172.265625, -240), (179.296875, -240), (186.328125, -240), (193.359375, -240),
                            (200.390625, -240), (207.421875, -240), (214.453125, -240), (221.484375, -240),
                            (228.515625, -240), (235.546875, -240), (242.578125, -240), (249.609375, -240),
                            (256.640625, -240), (263.671875, -240), (270.703125, -240), (277.734375, -240),
                            (284.765625, -240), (291.796875, -240), (298.828125, -240), (305.859375, -240),
                            (312.890625, -240), (319.921875, -240), (326.953125, -240), (333.984375, -240),
                            (341.015625, -240), (348.046875, -240), (355.078125, -240), (362.109375, -240),
                            (369.140625, -240), (376.171875, -240), (383.203125, -240), (390.234375, -240),
                            (397.265625, -240), (404.296875, -240), (411.328125, -240), (418.359375, -240),
                            (425.390625, -240), (432.421875, -240), (439.453125, -240), (446.484375, -240),
                            (453.515625, -240), (460.546875, -240), (467.578125, -240), (474.609375, -240),
                            (481.640625, -240), (488.671875, -240), (495.703125, -240), (502.734375, -240),
                            (509.765625, -240), (516.796875, -240), (523.828125, -240), (530.859375, -240),
                            (537.890625, -240), (544.921875, -240), (551.953125, -240), (558.984375, -240),
                            (566.015625, -240), (573.046875, -240), (580.078125, -240), (587.109375, -240),
                            (594.140625, -240), (601.171875, -240), (608.203125, -240), (615.234375, -240),
                            (622.265625, -240), (629.296875, -240), (636.328125, -240), (643.359375, -240),
                            (650.390625, -240), (657.421875, -240), (664.453125, -240), (671.484375, -240),
                            (678.515625, -240), (685.546875, -240), (692.578125, -240), (699.609375, -240),
                            (706.640625, -240), (713.671875, -240), (720.703125, -240), (727.734375, -240),
                            (734.765625, -240), (741.796875, -240), (748.828125, -240), (755.859375, -240),
                            (762.890625, -240), (769.921875, -240), (776.953125, -240), (783.984375, -240),
                            (791.015625, -240), (798.046875, -240), (805.078125, -240), (812.109375, -240),
                            (819.140625, -240), (826.171875, -240), (833.203125, -240), (840.234375, -240),
                            (847.265625, -240), (854.296875, -240), (861.328125, -240), (868.359375, -240),
                            (875.390625, -240), (882.421875, -240), (889.453125, -240), (896.484375, -240),
                            (-898.2421875, -300), (-894.7265625, -300), (-891.2109375, -300), (-887.6953125, -300),
                            (-884.1796875, -300), (-880.6640625, -300), (-877.1484375, -300), (-873.6328125, -300),
                            (-870.1171875, -300), (-866.6015625, -300), (-863.0859375, -300), (-859.5703125, -300),
                            (-856.0546875, -300), (-852.5390625, -300), (-849.0234375, -300), (-845.5078125, -300),
                            (-841.9921875, -300), (-838.4765625, -300), (-834.9609375, -300), (-831.4453125, -300),
                            (-827.9296875, -300), (-824.4140625, -300), (-820.8984375, -300), (-817.3828125, -300),
                            (-813.8671875, -300), (-810.3515625, -300), (-806.8359375, -300), (-803.3203125, -300),
                            (-799.8046875, -300), (-796.2890625, -300), (-792.7734375, -300), (-789.2578125, -300),
                            (-785.7421875, -300), (-782.2265625, -300), (-778.7109375, -300), (-775.1953125, -300),
                            (-771.6796875, -300), (-768.1640625, -300), (-764.6484375, -300), (-761.1328125, -300),
                            (-757.6171875, -300), (-754.1015625, -300), (-750.5859375, -300), (-747.0703125, -300),
                            (-743.5546875, -300), (-740.0390625, -300), (-736.5234375, -300), (-733.0078125, -300),
                            (-729.4921875, -300), (-725.9765625, -300), (-722.4609375, -300), (-718.9453125, -300),
                            (-715.4296875, -300), (-711.9140625, -300), (-708.3984375, -300), (-704.8828125, -300),
                            (-701.3671875, -300), (-697.8515625, -300), (-694.3359375, -300), (-690.8203125, -300),
                            (-687.3046875, -300), (-683.7890625, -300), (-680.2734375, -300), (-676.7578125, -300),
                            (-673.2421875, -300), (-669.7265625, -300), (-666.2109375, -300), (-662.6953125, -300),
                            (-659.1796875, -300), (-655.6640625, -300), (-652.1484375, -300), (-648.6328125, -300),
                            (-645.1171875, -300), (-641.6015625, -300), (-638.0859375, -300), (-634.5703125, -300),
                            (-631.0546875, -300), (-627.5390625, -300), (-624.0234375, -300), (-620.5078125, -300),
                            (-616.9921875, -300), (-613.4765625, -300), (-609.9609375, -300), (-606.4453125, -300),
                            (-602.9296875, -300), (-599.4140625, -300), (-595.8984375, -300), (-592.3828125, -300),
                            (-588.8671875, -300), (-585.3515625, -300), (-581.8359375, -300), (-578.3203125, -300),
                            (-574.8046875, -300), (-571.2890625, -300), (-567.7734375, -300), (-564.2578125, -300),
                            (-560.7421875, -300), (-557.2265625, -300), (-553.7109375, -300), (-550.1953125, -300),
                            (-546.6796875, -300), (-543.1640625, -300), (-539.6484375, -300), (-536.1328125, -300),
                            (-532.6171875, -300), (-529.1015625, -300), (-525.5859375, -300), (-522.0703125, -300),
                            (-518.5546875, -300), (-515.0390625, -300), (-511.5234375, -300), (-508.0078125, -300),
                            (-504.4921875, -300), (-500.9765625, -300), (-497.4609375, -300), (-493.9453125, -300),
                            (-490.4296875, -300), (-486.9140625, -300), (-483.3984375, -300), (-479.8828125, -300),
                            (-476.3671875, -300), (-472.8515625, -300), (-469.3359375, -300), (-465.8203125, -300),
                            (-462.3046875, -300), (-458.7890625, -300), (-455.2734375, -300), (-451.7578125, -300),
                            (-448.2421875, -300), (-444.7265625, -300), (-441.2109375, -300), (-437.6953125, -300),
                            (-434.1796875, -300), (-430.6640625, -300), (-427.1484375, -300), (-423.6328125, -300),
                            (-420.1171875, -300), (-416.6015625, -300), (-413.0859375, -300), (-409.5703125, -300),
                            (-406.0546875, -300), (-402.5390625, -300), (-399.0234375, -300), (-395.5078125, -300),
                            (-391.9921875, -300), (-388.4765625, -300), (-384.9609375, -300), (-381.4453125, -300),
                            (-377.9296875, -300), (-374.4140625, -300), (-370.8984375, -300), (-367.3828125, -300),
                            (-363.8671875, -300), (-360.3515625, -300), (-356.8359375, -300), (-353.3203125, -300),
                            (-349.8046875, -300), (-346.2890625, -300), (-342.7734375, -300), (-339.2578125, -300),
                            (-335.7421875, -300), (-332.2265625, -300), (-328.7109375, -300), (-325.1953125, -300),
                            (-321.6796875, -300), (-318.1640625, -300), (-314.6484375, -300), (-311.1328125, -300),
                            (-307.6171875, -300), (-304.1015625, -300), (-300.5859375, -300), (-297.0703125, -300),
                            (-293.5546875, -300), (-290.0390625, -300), (-286.5234375, -300), (-283.0078125, -300),
                            (-279.4921875, -300), (-275.9765625, -300), (-272.4609375, -300), (-268.9453125, -300),
                            (-265.4296875, -300), (-261.9140625, -300), (-258.3984375, -300), (-254.8828125, -300),
                            (-251.3671875, -300), (-247.8515625, -300), (-244.3359375, -300), (-240.8203125, -300),
                            (-237.3046875, -300), (-233.7890625, -300), (-230.2734375, -300), (-226.7578125, -300),
                            (-223.2421875, -300), (-219.7265625, -300), (-216.2109375, -300), (-212.6953125, -300),
                            (-209.1796875, -300), (-205.6640625, -300), (-202.1484375, -300), (-198.6328125, -300),
                            (-195.1171875, -300), (-191.6015625, -300), (-188.0859375, -300), (-184.5703125, -300),
                            (-181.0546875, -300), (-177.5390625, -300), (-174.0234375, -300), (-170.5078125, -300),
                            (-166.9921875, -300), (-163.4765625, -300), (-159.9609375, -300), (-156.4453125, -300),
                            (-152.9296875, -300), (-149.4140625, -300), (-145.8984375, -300), (-142.3828125, -300),
                            (-138.8671875, -300), (-135.3515625, -300), (-131.8359375, -300), (-128.3203125, -300),
                            (-124.8046875, -300), (-121.2890625, -300), (-117.7734375, -300), (-114.2578125, -300),
                            (-110.7421875, -300), (-107.2265625, -300), (-103.7109375, -300), (-100.1953125, -300),
                            (-96.6796875, -300), (-93.1640625, -300), (-89.6484375, -300), (-86.1328125, -300),
                            (-82.6171875, -300), (-79.1015625, -300), (-75.5859375, -300), (-72.0703125, -300),
                            (-68.5546875, -300), (-65.0390625, -300), (-61.5234375, -300), (-58.0078125, -300),
                            (-54.4921875, -300), (-50.9765625, -300), (-47.4609375, -300), (-43.9453125, -300),
                            (-40.4296875, -300), (-36.9140625, -300), (-33.3984375, -300), (-29.8828125, -300),
                            (-26.3671875, -300), (-22.8515625, -300), (-19.3359375, -300), (-15.8203125, -300),
                            (-12.3046875, -300), (-8.7890625, -300), (-5.2734375, -300), (-1.7578125, -300),
                            (1.7578125, -300), (5.2734375, -300), (8.7890625, -300), (12.3046875, -300),
                            (15.8203125, -300), (19.3359375, -300), (22.8515625, -300), (26.3671875, -300),
                            (29.8828125, -300), (33.3984375, -300), (36.9140625, -300), (40.4296875, -300),
                            (43.9453125, -300), (47.4609375, -300), (50.9765625, -300), (54.4921875, -300),
                            (58.0078125, -300), (61.5234375, -300), (65.0390625, -300), (68.5546875, -300),
                            (72.0703125, -300), (75.5859375, -300), (79.1015625, -300), (82.6171875, -300),
                            (86.1328125, -300), (89.6484375, -300), (93.1640625, -300), (96.6796875, -300),
                            (100.1953125, -300), (103.7109375, -300), (107.2265625, -300), (110.7421875, -300),
                            (114.2578125, -300), (117.7734375, -300), (121.2890625, -300), (124.8046875, -300),
                            (128.3203125, -300), (131.8359375, -300), (135.3515625, -300), (138.8671875, -300),
                            (142.3828125, -300), (145.8984375, -300), (149.4140625, -300), (152.9296875, -300),
                            (156.4453125, -300), (159.9609375, -300), (163.4765625, -300), (166.9921875, -300),
                            (170.5078125, -300), (174.0234375, -300), (177.5390625, -300), (181.0546875, -300),
                            (184.5703125, -300), (188.0859375, -300), (191.6015625, -300), (195.1171875, -300),
                            (198.6328125, -300), (202.1484375, -300), (205.6640625, -300), (209.1796875, -300),
                            (212.6953125, -300), (216.2109375, -300), (219.7265625, -300), (223.2421875, -300),
                            (226.7578125, -300), (230.2734375, -300), (233.7890625, -300), (237.3046875, -300),
                            (240.8203125, -300), (244.3359375, -300), (247.8515625, -300), (251.3671875, -300),
                            (254.8828125, -300), (258.3984375, -300), (261.9140625, -300), (265.4296875, -300),
                            (268.9453125, -300), (272.4609375, -300), (275.9765625, -300), (279.4921875, -300),
                            (283.0078125, -300), (286.5234375, -300), (290.0390625, -300), (293.5546875, -300),
                            (297.0703125, -300), (300.5859375, -300), (304.1015625, -300), (307.6171875, -300),
                            (311.1328125, -300), (314.6484375, -300), (318.1640625, -300), (321.6796875, -300),
                            (325.1953125, -300), (328.7109375, -300), (332.2265625, -300), (335.7421875, -300),
                            (339.2578125, -300), (342.7734375, -300), (346.2890625, -300), (349.8046875, -300),
                            (353.3203125, -300), (356.8359375, -300), (360.3515625, -300), (363.8671875, -300),
                            (367.3828125, -300), (370.8984375, -300), (374.4140625, -300), (377.9296875, -300),
                            (381.4453125, -300), (384.9609375, -300), (388.4765625, -300), (391.9921875, -300),
                            (395.5078125, -300), (399.0234375, -300), (402.5390625, -300), (406.0546875, -300),
                            (409.5703125, -300), (413.0859375, -300), (416.6015625, -300), (420.1171875, -300),
                            (423.6328125, -300), (427.1484375, -300), (430.6640625, -300), (434.1796875, -300),
                            (437.6953125, -300), (441.2109375, -300), (444.7265625, -300), (448.2421875, -300),
                            (451.7578125, -300), (455.2734375, -300), (458.7890625, -300), (462.3046875, -300),
                            (465.8203125, -300), (469.3359375, -300), (472.8515625, -300), (476.3671875, -300),
                            (479.8828125, -300), (483.3984375, -300), (486.9140625, -300), (490.4296875, -300),
                            (493.9453125, -300), (497.4609375, -300), (500.9765625, -300), (504.4921875, -300),
                            (508.0078125, -300), (511.5234375, -300), (515.0390625, -300), (518.5546875, -300),
                            (522.0703125, -300), (525.5859375, -300), (529.1015625, -300), (532.6171875, -300),
                            (536.1328125, -300), (539.6484375, -300), (543.1640625, -300), (546.6796875, -300),
                            (550.1953125, -300), (553.7109375, -300), (557.2265625, -300), (560.7421875, -300),
                            (564.2578125, -300), (567.7734375, -300), (571.2890625, -300), (574.8046875, -300),
                            (578.3203125, -300), (581.8359375, -300), (585.3515625, -300), (588.8671875, -300),
                            (592.3828125, -300), (595.8984375, -300), (599.4140625, -300), (602.9296875, -300),
                            (606.4453125, -300), (609.9609375, -300), (613.4765625, -300), (616.9921875, -300),
                            (620.5078125, -300), (624.0234375, -300), (627.5390625, -300), (631.0546875, -300),
                            (634.5703125, -300), (638.0859375, -300), (641.6015625, -300), (645.1171875, -300),
                            (648.6328125, -300), (652.1484375, -300), (655.6640625, -300), (659.1796875, -300),
                            (662.6953125, -300), (666.2109375, -300), (669.7265625, -300), (673.2421875, -300),
                            (676.7578125, -300), (680.2734375, -300), (683.7890625, -300), (687.3046875, -300),
                            (690.8203125, -300), (694.3359375, -300), (697.8515625, -300), (701.3671875, -300),
                            (704.8828125, -300), (708.3984375, -300), (711.9140625, -300), (715.4296875, -300),
                            (718.9453125, -300), (722.4609375, -300), (725.9765625, -300), (729.4921875, -300),
                            (733.0078125, -300), (736.5234375, -300), (740.0390625, -300), (743.5546875, -300),
                            (747.0703125, -300), (750.5859375, -300), (754.1015625, -300), (757.6171875, -300),
                            (761.1328125, -300), (764.6484375, -300), (768.1640625, -300), (771.6796875, -300),
                            (775.1953125, -300), (778.7109375, -300), (782.2265625, -300), (785.7421875, -300),
                            (789.2578125, -300), (792.7734375, -300), (796.2890625, -300), (799.8046875, -300),
                            (803.3203125, -300), (806.8359375, -300), (810.3515625, -300), (813.8671875, -300),
                            (817.3828125, -300), (820.8984375, -300), (824.4140625, -300), (827.9296875, -300),
                            (831.4453125, -300), (834.9609375, -300), (838.4765625, -300), (841.9921875, -300),
                            (845.5078125, -300), (849.0234375, -300), (852.5390625, -300), (856.0546875, -300),
                            (859.5703125, -300), (863.0859375, -300), (866.6015625, -300), (870.1171875, -300),
                            (873.6328125, -300), (877.1484375, -300), (880.6640625, -300), (884.1796875, -300),
                            (887.6953125, -300), (891.2109375, -300), (894.7265625, -300), (898.2421875, -300)]

    def drawtree(self, plusdepth=0, verticaloffset=-300, rebuildcoordinates=False):
        heap = self.heap
        t = self.turtle
        screen = tut.Screen()

        screen.setup(width=1.0, height=1.0)

        t.speed(0)
        t.penup()

        depth = math.ceil(len(heap) // 2) + plusdepth
        width = depth * 100

        if len(self.coordinates) <= 0 or rebuildcoordinates:
            verticalspacing = 60
            down = 1
            curx = width
            cury = verticaloffset
            for i in range(depth, -1, -1):
                for j in range(2 ** i):
                    curx -= width / 2 ** i
                    self.coordinates.append((curx, cury))
                    curx -= width / 2 ** i
                curx = width
                cury = down * verticalspacing + verticaloffset
                down += 1
            self.coordinates.reverse()

        self.fill_tree()
        screen.exitonclick()

    def writefun(self, item_idx):
        font = ("Times New Roman", 12, "normal")
        align = "center"
        text = f'Val: {self.heap[item_idx]}'

        self.turtle.pendown()
        self.turtle.circle(20)
        self.turtle.write(arg=text, align=align, font=font)
        self.turtle.penup()

    def fill_tree(self, curcoord=0, item_idx=None):
        coords = self.coordinates
        t = self.turtle
        heap = self.heap
        if item_idx is None:
            item_idx = 0

        t.goto(coords[curcoord])
        self.writefun(item_idx)

        leftchild_idx = 2 * curcoord + 1
        rightchild_idx = 2 * curcoord + 2

        if leftchild_idx < len(heap):
            t.goto(coords[curcoord])
            t.pendown()
            self.fill_tree(2 * curcoord + 1, leftchild_idx)
            t.penup()

        if rightchild_idx < len(heap):
            t.goto(coords[curcoord])
            t.pendown()
            self.fill_tree(2 * curcoord + 2, rightchild_idx)
            t.penup()

class binary_treeNAR():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_root_val(self):
        return self.value

    def set_root_val(self, val):
        self.value = val

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def insert_left(self, val):
        child = self.left
        if self.left is None:
            self.left = binary_treeNAR(val)
        else:
            self.left = binary_treeNAR(val)
            self.left.insert_left(child)

    def insert_right(self, val):
        child = self.right
        if self.right is None:
            self.right = binary_treeNAR(val)
        else:
            self.right = binary_treeNAR(val)
            self.right.insert_right(child)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, z):
        return self.stack.append(z)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


class ParseTree(binary_treeNAR):
    def __init__(self, value=None):
        super().__init__(value)

    def handle_existingdigits(self, char, peek):
        if peek and isinstance(peek.get_root_val(), str):
            return peek.get_root_val() + char
        return char

    def str_to_tree(self, val):
        tree = binary_treeNAR()
        treestack = Stack()
        treestack.push(tree)
        for char in val[1:len(val) - 1]:
            cur_tree = treestack.peek()
            if char == '(':
                if cur_tree.get_left_child() is None:
                    cur_tree.insert_left(None)
                    treestack.push(cur_tree.get_left_child())
                else:
                    cur_tree.insert_right(None)
                    treestack.push(cur_tree.get_right_child())
            elif char == ')':
                treestack.pop()
            elif char in '+-*/':
                cur_tree.set_root_val(char)
            elif char.isnumeric():
                if cur_tree.get_root_val() is None:
                    insert = self.handle_existingdigits(char, cur_tree.get_left_child())
                    cur_tree.left = None
                    cur_tree.insert_left(insert)
                else:
                    insert = self.handle_existingdigits(char, cur_tree.get_right_child())
                    cur_tree.right = None
                    cur_tree.insert_right(insert)
            elif char == ' ':
                continue
            else:
                raise Exception('Unhandled operator', char)
        return tree

    def tree_to_eval(self, node):
        operators = {"+": ops.add,
                     "-": ops.sub,
                     "/": ops.truediv,
                     "*": ops.mul}

        if not node.get_right_child() and not node.get_left_child():
            return node.get_root_val()

        operator = operators[node.get_root_val()]
        operand1 = self.tree_to_eval(node.get_left_child())
        operand2 = self.tree_to_eval(node.get_right_child())

        return operator(int(operand1), int(operand2))

    def tree_to_str(self, node):
        res = ''
        operand1 = node.get_left_child()
        operand2 = node.get_right_child()
        if not operand1 and not operand2:
            return node.get_root_val() + ''

        res += '(' + self.tree_to_str(operand1) + ' ' + node.get_root_val() + ' ' + self.tree_to_str(operand2) + ')'
        return res