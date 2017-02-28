Clear the models trained, but without the one with highest validation accuracy.

The data should be named something like:

000_epoch-2.7711_loss-0.2986_acc-5.1066_val_loss-0.1320_val_acc.hdf5
001_epoch-1.2082_loss-0.6824_acc-3.9153_val_loss-0.1771_val_acc.hdf5
002_epoch-0.4490_loss-0.8874_acc-4.3705_val_loss-0.1850_val_acc.hdf5
003_epoch-0.2349_loss-0.9409_acc-4.2997_val_loss-0.1804_val_acc.hdf5
004_epoch-0.1669_loss-0.9594_acc-4.0582_val_loss-0.1987_val_acc.hdf5
005_epoch-0.1229_loss-0.9728_acc-4.4224_val_loss-0.1948_val_acc.hdf5
006_epoch-0.0931_loss-0.9801_acc-4.3635_val_loss-0.1908_val_acc.hdf5
007_epoch-0.0816_loss-0.9815_acc-4.4561_val_loss-0.2065_val_acc.hdf5
008_epoch-0.0677_loss-0.9874_acc-4.0762_val_loss-0.2137_val_acc.hdf5
009_epoch-0.0516_loss-0.9905_acc-4.4360_val_loss-0.2092_val_acc.hdf5

If you run this code at the directory, it will clear everything except for 008 epoch. And it'll log the files into result.log at the directory so that you still don't lose the results.

HINT: set the directory of this code as PATH, so that you can easily run this code at the directory.
