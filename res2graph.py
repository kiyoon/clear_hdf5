#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description='Read the result.log file and save it to csv and graphs.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-i", "--input", type=str, default='result.log',
        help='input log file to read')
parser.add_argument("-o", "--output-csv", type=str, default='result.csv', 
        help='output csv file path')
parser.add_argument("-l", "--output-loss", type=str, default='loss.pdf', 
        help='output loss graph file path')
parser.add_argument("-a", "--output-acc", type=str, default='acc.pdf', 
        help='output acc graph file path')
parser.add_argument("--loss-range", type=float, nargs=2, default=None, 
        help='plot range for loss')
parser.add_argument("--acc-range", type=float, nargs=2, default=None, 
        help='plot range for acc')

args = parser.parse_args()

import matplotlib.pyplot as plt
plt.style.use('ggplot')

from statistics import stdev

labels = ['epoch', 'loss(train)', 'acc(train)', 'loss(valid)', 'acc(valid)']
data = {}
for label in labels:
    data[label] = []        # initialise the dictionary with empty lists


# read
with open(args.input, "r") as f:
    log = f.read()

# save csv and rearrange the data
with open(args.output_csv, "w") as f:
    f.write(','.join(labels) + '\n')
    lines = log.split('\n')
    for line in lines:
        if line:    # is it not empty?
            components = line.split('-')
            for i, component in enumerate(components):
                value = component.split('_')[0]
                num_value = float(value) if i!=0 else int(value)    # epoch is int, the rest is float
                f.write(value + ',')
                data[labels[i]].append(num_value)
            f.write('\n')




# save plots
fig_1 = plt.figure(figsize=(8, 4))
ax_1 = fig_1.add_subplot(111)
ax_1.set_xlim([min(data['epoch'])-1,max(data['epoch'])+1])
if args.loss_range is None:
    all_loss = data['loss(train)'] + data['loss(valid)']
    std = stdev(all_loss)
    ax_1.set_ylim([min(all_loss)-0.1*std,max(all_loss)+0.1*std])
else:
    ax_1.set_ylim(args.loss_range)

for k in ['loss(train)', 'loss(valid)']:
    ax_1.plot(data['epoch'], 
	      data[k], label=k)
ax_1.legend(loc=0)
ax_1.set_xlabel('Epoch number')

# Plot the change in the validation and training set accuracy over training.
fig_2 = plt.figure(figsize=(8, 4))
ax_2 = fig_2.add_subplot(111)
ax_2.set_xlim([min(data['epoch'])-1,max(data['epoch'])+1])
if args.acc_range is None:
    all_acc = data['acc(train)'] + data['acc(valid)']
    std = stdev(all_acc)
    ax_2.set_ylim([min(all_acc)-0.1*std,max(all_acc)+0.1*std])
else:
    ax_2.set_ylim(args.acc_range)
for k in ['acc(train)', 'acc(valid)']:
    ax_2.plot(data['epoch'], 
	      data[k], label=k)
ax_2.legend(loc=0)
ax_2.set_xlabel('Epoch number')

fig_1.tight_layout()
fig_1.savefig(args.output_loss)
fig_2.tight_layout()
fig_2.savefig(args.output_acc)
