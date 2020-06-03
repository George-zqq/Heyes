# -*- coding:utf-8 -*-
import sys
from HDFS.prometheus_namenode import hdfsExporter
from flask import Response, Flask
from prometheus_client import Gauge, Counter, Enum, CollectorRegistry, generate_latest
from configparser import ConfigParser
from YARN.yarnexporter import yarnexporter

app = Flask(__name__)

config = ConfigParser()
config.readfp(open('../conf/config.ini'))


@app.route('/metrics/dfs')
def dfsmetric():
    Registry = CollectorRegistry()
    dfsurl = config.get('dfs_jmx_url', 'url')
    exporter = hdfsExporter(dfsurl)

    heapused = Gauge('hdfs_namenodeheap', 'Descriptionofgauge', ['cluster', 'service'], registry=Registry)
    blockscorrupt = Gauge('hdfs_blockscorrupt', 'Corrupted Block Number', ['cluster', 'service'], registry=Registry)
    numNodes = Gauge('hdfs_NumNodes', 'Alive Nodes', ['cluster', 'service'], registry=Registry)
    capUsed = Gauge('hdfs_CapacityUsed', 'capacity used', ['cluster', 'service'], registry=Registry)
    rpcConn = Gauge('hdfs_NumOpenConnections', 'open rpc Conn', ['cluster', 'service'], registry=Registry)
    totalFile = Gauge('hdfs_TotalFiles', 'hdfs total files', ['cluster', 'service'], registry=Registry)
    totalBlock = Gauge('hdfs_TotalBlocks', 'hdfs total block', ['cluster', 'service'], registry=Registry)
    underReplicatedBlock = Gauge('hdfs_UnderReplicatedBlocks', 'hdfs under rep blocks', ['cluster', 'service'],
                                 registry=Registry)
    missingBlock = Gauge('hdfs_MissingBlocks', 'hdfs Miss blocks', ['cluster', 'service'], registry=Registry)
    excessBlock = Gauge('hdfs_ExcessBlocks', 'hdfs excess blocks', ['cluster', 'service'], registry=Registry)
    lastCheckpointTime = Gauge('hdfs_lastCheckPoint', 'hdfs last checkpoint time', ['cluster', 'service'],
                               registry=Registry)
    numLiveDataNode = Gauge('hdfs_AliveNodes', 'number of live nodes', ['cluster', 'service'], registry=Registry)
    numDeadDataNode = Gauge('hdfs_DeadNodes', 'number of dead nodes', ['cluster', 'service'], registry=Registry)
    numStaleDataNode = Gauge('hdfs_StaleNodes', 'number of stale nodes', ['cluster', 'service'], registry=Registry)
    lastHATransitionTime = Gauge('hdfs_HATransitionTime', 'last HA Trans time', ['cluster', 'service'],
                                 registry=Registry)
    totalLoad = Gauge('hdfs_TotalLoad', 'number of xceiver', ['cluster', 'service'], registry=Registry)
    receivedByte = Gauge('hdfs_ReceivedBytes', 'namenode received bytes', ['cluster', 'service'], registry=Registry)
    sentByte = Gauge('hdfs_SentBytes', 'namenode sent bytes', ['cluster', 'service'], registry=Registry)
    capacityRemainingGB = Gauge('hdfs_CapacityRemainingGB', 'hdfs remain capacity', ['cluster', 'service'],
                                registry=Registry)
    capacityUsedGB = Gauge('hdfs_CapacityUsedGB', 'hdfs used capacity', ['cluster', 'service'], registry=Registry)
    capacityTotalGB = Gauge('hdfs_CapacityTotalGB', 'hdfs total capacity', ['cluster', 'service'], registry=Registry)
    blockCapacity = Gauge('hdfs_BlockCapacity', 'hdfs block capacity', ['cluster', 'service'], registry=Registry)
    pendingDeletionBlocks = Gauge('hdfs_PendingDeletionBlocks', 'hdfs none Deletion capacity', ['cluster', 'service'],
                                  registry=Registry)
    missingReplOneBlocks = Gauge('hdfs_MissingReplOneBlocks', 'hdfs miss rep blocks', ['cluster', 'service'],
                                 registry=Registry)
    numTimedOutPendingRep = Gauge('hdfs_NumTimedOutPendingRep', 'Number of hdfs Pending Replication',
                                  ['cluster', 'service'], registry=Registry)
    numActiveClients = Gauge('hdfs_NumActiveClients', 'number of hdfs active clients', ['cluster', 'service'],
                             registry=Registry)
    threadsNew = Gauge('hdfs_ThreadsNew', 'number of namenode threadsNew', ['cluster', 'service'], registry=Registry)
    threadsRunnable = Gauge('hdfs_ThreadsRunnable', 'number of namenode threads Runnable', ['cluster', 'service'],
                            registry=Registry)
    threadsBlocked = Gauge('hdfs_ThreadsBlocked', 'number of namenode threadsBlocked', ['cluster', 'service'],
                           registry=Registry)
    threadsWaiting = Gauge('hdfs_ThreadsWaiting', 'number of namenode threadsWaiting', ['cluster', 'service'],
                           registry=Registry)
    threadsTimedWaiting = Gauge('hdfs_ThreadsTimedWaiting', 'number of namenode threadsTimedWaiting',
                                ['cluster', 'service'], registry=Registry)
    threadsTerminated = Gauge('hdfs_ThreadsTerminated', 'number of namenode threadsTerminated', ['cluster', 'service'],
                              registry=Registry)

    heapused.labels(cluster='bdp-online', service='hdfs').set(exporter.get_nnHeap_utilization())
    blockscorrupt.labels(cluster='bdp-online', service='hdfs').set(exporter.get_dfs_corruptedBlocks())
    numNodes.labels(cluster='bdp-online', service='hdfs').set(exporter.get_numAliveNodes())
    capUsed.labels(cluster='bdp-online', service='hdfs').set(exporter.get_dfs_utilization())
    rpcConn.labels(cluster='bdp-online', service='hdfs').set(exporter.get_nn_rpcConn())
    totalFile.labels(cluster='bdp-online', service='hdfs').set(exporter.get_dfs_totalFiles())
    totalBlock.labels(cluster='bdp-online', service='hdfs').set(exporter.get_dfs_totalBlocks())
    underReplicatedBlock.labels(cluster='bdp-online', service='hdfs').set(exporter.get_dfs_UnderReplicatedBlocks())
    missingBlock.labels(cluster='bdp-online', service='hdfs').set(exporter.get_dfs_missBlocks())
    excessBlock.labels(cluster='bdp-online', service='hdfs').set(exporter.get_dfs_excessBlocks())
    lastCheckpointTime.labels(cluster='bdp-online', service='hdfs').set(exporter.get_dfs_LastCheckpointTime())

    numLiveDataNode.labels(cluster='bdp-online', service='hdfs').set(exporter.get_numAliveNodes())
    numDeadDataNode.labels(cluster='bdp-online', service='hdfs').set(exporter.get_numDeadNodes())
    numStaleDataNode.labels(cluster='bdp-online', service='hdfs').set(exporter.get_staleNodes())
    lastHATransitionTime.labels(cluster='bdp-online', service='hdfs').set(exporter.get_lastHaTrans())
    totalLoad.labels(cluster='bdp-online', service='hdfs').set(exporter.get_TotalLoad())

    receivedByte.labels(cluster='bdp-online', service='hdfs').set(exporter.get_receivedBytes())
    sentByte.labels(cluster='bdp-online', service='hdfs').set(exporter.get_sentdBytes())

    capacityRemainingGB.labels(cluster='bdp-online', service='hdfs').set(exporter.get_capacityRemainingGB())
    capacityUsedGB.labels(cluster='bdp-online', service='hdfs').set(exporter.get_capacityUsedGB())
    capacityTotalGB.labels(cluster='bdp-online', service='hdfs').set(exporter.get_capacityTotalGB())
    blockCapacity.labels(cluster='bdp-online', service='hdfs').set(exporter.get_blockCapacity())
    pendingDeletionBlocks.labels(cluster='bdp-online', service='hdfs').set(exporter.get_PendingDeletionBlocks())
    numTimedOutPendingRep.labels(cluster='bdp-online', service='hdfs').set(
        exporter.get_numTimedOutPendingReplications())
    numActiveClients.labels(cluster='bdp-online', service='hdfs').set(exporter.get_numActiveClients())
    missingReplOneBlocks.labels(cluster='bdp-online', service='hdfs').set(exporter.get_MissingReplOneBlocks())
    threadsNew.labels(cluster='bdp-online', service='hdfs').set(exporter.get_jvm_ThreadsNew())
    threadsRunnable.labels(cluster='bdp-online', service='hdfs').set(exporter.get_jvm_ThreadsRunnable())
    threadsBlocked.labels(cluster='bdp-online', service='hdfs').set(exporter.get_jvm_ThreadsBlocked())
    threadsWaiting.labels(cluster='bdp-online', service='hdfs').set(exporter.get_jvm_ThreadsWaiting())
    threadsTimedWaiting.labels(cluster='bdp-online', service='hdfs').set(exporter.get_jvm_ThreadsTimedWaiting())
    threadsTerminated.labels(cluster='bdp-online', service='hdfs').set(exporter.get_jvm_ThreadsTerminated())

    return Response(generate_latest(Registry), mimetype='text/plain')


@app.route('/metric/yarn')
def yarnmetric():
    Registry = CollectorRegistry()
    yarnurl = config.get('yarn_jmx_url', 'url')
    yarner = yarnexporter(yarnurl)

    """
      RM jvm metric 
    """
    jvmdata = yarner.get_rmJvmMetric()
    memheapMax = Gauge('yarn_rm_heapmax', 'Description of RM', ['cluster', 'service'], registry=Registry)
    memheapMax.labels(cluster='bdp-online', service='yarn').set(jvmdata['MemHeapMaxM'])

    heapused = Gauge('yarn_rm_heapused', 'Description of RM', ['cluster', 'service'], registry=Registry)
    heapused.labels(cluster='bdp-online', service='yarn').set(jvmdata['MemNonHeapUsedM'])

    gcCount = Gauge('yarn_rm_gcCount', 'Description of RM', ['cluster', 'service'], registry=Registry)
    gcCount.labels(cluster='bdp-online', service='yarn').set(jvmdata['GcCount'])

    tnew = Gauge('yarn_rm_threadNew', 'Description of RM', ['cluster', 'service'], registry=Registry)
    tnew.labels(cluster='bdp-online', service='yarn').set(jvmdata['ThreadsNew'])

    trun = Gauge('yarn_rm_threadRunnable', 'Description of RM', ['cluster', 'service'], registry=Registry)
    trun.labels(cluster='bdp-online', service='yarn').set(jvmdata['ThreadsRunnable'])

    tb = Gauge('yarn_rm_threadBlocked', 'Description of RM', ['cluster', 'service'], registry=Registry)
    tb.labels(cluster='bdp-online', service='yarn').set(jvmdata['ThreadsBlocked'])

    tw = Gauge('yarn_rm_threadWaiting', 'Description of RM', ['cluster', 'service'], registry=Registry)
    tw.labels(cluster='bdp-online', service='yarn').set(jvmdata['ThreadsWaiting'])

    ttw = Gauge('yarn_rm_threadTimeWaiting', 'Description of RM', ['cluster', 'service'], registry=Registry)
    ttw.labels(cluster='bdp-online', service='yarn').set(jvmdata['ThreadsTimedWaiting'])

    tt = Gauge('yarn_rm_threadTerminated', 'Description of RM', ['cluster', 'service'], registry=Registry)
    tt.labels(cluster='bdp-online', service='yarn').set(jvmdata['ThreadsTerminated'])

    logw = Gauge('yarn_rm_logWarn', 'Description of RM', ['cluster', 'service'], registry=Registry)
    logw.labels(cluster='bdp-online', service='yarn').set(jvmdata['LogWarn'])

    loge = Gauge('yarn_rm_logError', 'Description of RM', ['cluster', 'service'], registry=Registry)
    loge.labels(cluster='bdp-online', service='yarn').set(jvmdata['LogError'])

    """
    Queue Metric data
    """
    queueMetricdata = yarner.get_queueMetric()
    appRunning = Gauge('yarn_queue_apprunning', 'Description of RM', ['cluster', 'service'], registry=Registry)
    appRunning.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['AppsRunning'])

    appPending = Gauge('yarn_queue_appPending', 'Description of RM', ['cluster', 'service'], registry=Registry)
    appPending.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['AppsPending'])

    appsSubmitted = Gauge('yarn_queue_appsSubmitted', 'Description of RM', ['cluster', 'service'], registry=Registry)
    appsSubmitted.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['AppsSubmitted'])

    appsCompleted = Gauge('yarn_queue_appsCompleted', 'Description of RM', ['cluster', 'service'], registry=Registry)
    appsCompleted.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['AppsCompleted'])

    appsKilled = Gauge('yarn_queue_appsKilled', 'Description of RM', ['cluster', 'service'], registry=Registry)
    appsKilled.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['AppsKilled'])

    appsFailed = Gauge('yarn_queue_appsFailed', 'Description of RM', ['cluster', 'service'], registry=Registry)
    appsFailed.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['AppsFailed'])

    allocatedMB = Gauge('yarn_queue_allocatedMB', 'Description of RM', ['cluster', 'service'], registry=Registry)
    allocatedMB.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['AllocatedMB'])

    allocatedVCores = Gauge('yarn_queue_allocatedVCores', 'Description of RM', ['cluster', 'service'],registry=Registry)
    allocatedVCores.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['AllocatedVCores'])

    allocatedContainers = Gauge('yarn_queue_allocatedContainers', 'Description of RM', ['cluster', 'service'],registry=Registry)
    allocatedContainers.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['AllocatedContainers'])

    availableMB = Gauge('yarn_queue_availableMB', 'Description of RM', ['cluster', 'service'], registry=Registry)
    availableMB.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['AvailableMB'])

    availableVCores = Gauge('yarn_queue_availableVCores', 'Description of RM', ['cluster', 'service'], registry=Registry)
    availableVCores.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['AvailableVCores'])

    pendingMB = Gauge('yarn_queue_pendingMB', 'Description of RM', ['cluster', 'service'], registry=Registry)
    pendingMB.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['PendingMB'])

    pendingVCores = Gauge('yarn_queue_pendingVCores', 'Description of RM', ['cluster', 'service'], registry=Registry)
    pendingVCores.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['PendingVCores'])

    pendingContainers = Gauge('yarn_queue_pendingContainers', 'Description of RM', ['cluster', 'service'],registry=Registry)
    pendingContainers.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['PendingContainers'])

    reservedMB = Gauge('yarn_queue_reservedMB', 'Description of RM', ['cluster', 'service'], registry=Registry)
    reservedMB.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['ReservedMB'])

    reservedVCores = Gauge('yarn_queue_reservedVCores', 'Description of RM', ['cluster', 'service'], registry=Registry)
    reservedVCores.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['ReservedVCores'])

    reservedContainers = Gauge('yarn_queue_reservedContainers', 'Description of RM', ['cluster', 'service'],registry=Registry)
    reservedContainers.labels(cluster='bdp-online', service='yarn').set(queueMetricdata['ReservedContainers'])

    "RMNM INFO"

    nmdata = yarner.get_rnnminfo()
    healtime = Gauge('nminfo_healthytime', 'Description of RM', ['host', 'service'], registry=Registry)
    numcontainer = Gauge('nminfo_container', 'Description of RM', ['host', 'service'], registry=Registry)
    useMemMB = Gauge('nminfo_useMemMB', 'Description of RM', ['host', 'service'], registry=Registry)
    avaiMemMB = Gauge('nminfo_avaiMemMB', 'Description of RM', ['host', 'service'], registry=Registry)
    for metric in nmdata:

        healtime.labels(host=metric['HostName'], service='healtime').set(metric['LastHealthUpdate'])
        numcontainer.labels(host=metric['HostName'], service='numcontainer').set(metric['NumContainers'])
        useMemMB.labels(host=metric['HostName'], service='useMemMB').set(metric['UsedMemoryMB'])
        avaiMemMB.labels(host=metric['HostName'], service='avaiMemMB').set(metric['AvailableMemoryMB'])
    return Response(generate_latest(Registry), mimetype='text/plain')













# @app.route('/metric/hive')
# def hivemetric():
# return Response(generate_latest(Registry), mimetype='text/plain')


# @app.route('/metric/hbase')
# def hbasemetric():
#  return Response(generate_latest(Registry), mimetype='text/plain')


# @app.route('/metric/zk')
# def zkmetric():
#   return Response(generate_latest(Registry), mimetype='text/plain')


# @app.route('/metric/presto')
# def prestometric():
#    return Response(generate_latest(Registry), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8765)
