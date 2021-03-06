#! -*- coding:utf-8 -*-
#!/bin/python
hadoop = {'bdp01.sa.cn': ['NameNode', 'ZeppelinServer', 'DFSZKFailoverController', 'JournalNode', 'ResourceManager'],
          'bdp02.sa.cn': ['NameNode', 'HMaster', 'DFSZKFailoverController', 'JobHistoryServer', 'JournalNode',
                          'ResourceManager'],
          'bdp03.sa.cn': ['NodeManager', 'DataNode', 'HRegionServer', 'HMaster', 'JournalNode'],
          'bdp04.sa.cn': ['NodeManager', 'DataNode', ],
          'bdp05.sa.cn': ['NodeManager', 'DataNode', 'LivyServer', 'HistoryServer'],
          'bdp06.sa.cn': ['NodeManager', 'DataNode'],
          'bdp07.sa.cn': ['QuorumPeerMain', 'Kafka'],
          'bdp08.sa.cn': ['QuorumPeerMain', 'Kafka'],
          'bdp09.sa.cn': ['QuorumPeerMain', 'Kafka'],
          'bdp10.sa.cn': ['Kafka', 'AzkabanExecutorServer'],
          'bdp11.sa.cn': ['QuorumPeerMain'],
          'bdp12.sa.cn': ['QuorumPeerMain', 'AzkabanExecutorServer'],
          'bdp13.sa.cn': ['NodeManager'],
          'bdp14.sa.cn': ['NodeManager', 'HRegionServer'],
          'bdp15.sa.cn': ['flume'],
          'bdp16.sa.cn': ['flume'],
          'bdp17.sa.cn': ['flume'],
          'bdp18.sa.cn': ['NodeManager', 'DataNode'],
          'bdp19.sa.cn': ['NodeManager', 'DataNode', 'LivyServer'],
          'bdp20.sa.cn': ['NodeManager', 'DataNode', 'HRegionServer', 'UnixAuthenticationService', 'EmbeddedServer'],
          'bdp21.sa.cn': ['NodeManager', 'DataNode', 'HRegionServer', 'HMaster'],
          'bdp22.sa.cn': ['NodeManager', 'DataNode', 'HRegionServer'],
          'bdp23.sa.cn': ['NodeManager', 'DataNode', 'HRegionServer'],
          'bdp24.sa.cn': ['Kafka'],
          'bdp25.sa.cn': ['Kafka'],
          'bdp26.sa.cn': ['flume'],
          'bdp27.sa.cn': ['flume'],
          'bdp28.sa.cn': ['NodeManager', 'DataNode'],
          'bdp29.sa.cn': ['NodeManager', 'DataNode'],
          'bdp30.sa.cn': ['NodeManager', 'DataNode'],
          'bdp31.sa.cn': ['NodeManager', 'DataNode'],
          'bdp32.sa.cn': ['NodeManager', 'DataNode'],
          'bdp33.sa.cn': ['NodeManager', 'DataNode'],
          'bdp34.sa.cn': ['NodeManager', 'DataNode'],
          'bdp35.sa.cn': ['NodeManager', 'DataNode'],
          'bdp36.sa.cn': ['NodeManager', 'DataNode'],
          'bdp37.sa.cn': ['flume'],
          'bdp38.sa.cn': ['NodeManager', 'DataNode'],
          'bdp39.sa.cn': ['NodeManager', 'DataNode'],
          'bdp40.sa.cn': ['NodeManager', 'DataNode'],
          'bdp41.sa.cn': ['NodeManager', 'DataNode'],
          'bdp42.sa.cn': ['NodeManager', 'DataNode'],
          'bdp43.sa.cn': ['NodeManager', 'DataNode'],
          'bdp44.sa.cn': ['NodeManager', 'DataNode'],
          'bdp45.sa.cn': ['NodeManager', 'DataNode'],
          'bdp46.sa.cn': ['NodeManager', 'DataNode'],
          'bdp47.sa.cn': ['NodeManager', 'DataNode'],
          'bdp48.sa.cn': ['NodeManager', 'DataNode'],
          'bdp49.sa.cn': ['NodeManager', 'DataNode'],
          'bdp50.sa.cn': ['NodeManager', 'DataNode'],
          'bdp51.sa.cn': ['NodeManager', 'DataNode'],
          'bdp52.sa.cn': ['NodeManager', 'DataNode'],
          'bdp53.sa.cn': ['NodeManager', 'DataNode'],
          'bdp54.sa.cn': ['flume'],
          'bdp55.sa.cn': ['flume']}
