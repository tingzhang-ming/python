# -*- coding:utf-8 -*-
import json
import os
import bottle
from god.common.utils import *
from mako.template import Template
from twitter.common.http import HttpServer, route, static_file

class GodServer(HttpServer):

    def __init__(self, scheduler, asset_dir):
      super(GodServer, self).__init__()
      self._scheduler = scheduler

      self._asset_dir = asset_dir
      self._static_dir = os.path.join(self._asset_dir, 'static')
      self._template_dir = os.path.join(self._asset_dir, 'templates')
      # self._clusters_template = Template(filename=os.path.join(self._template_dir, 'clusters.html'),input_encoding="utf-8")
      # self._nodes_template = Template(filename=os.path.join(self._template_dir, 'nodes.html'),input_encoding="utf-8")
      # self._create_template = Template(filename=os.path.join(self._template_dir, 'create.html'),input_encoding="utf-8")

    # add replication_user and replication_password to def create and try create_cluster
    @route('/createcluster', method=['POST'])
    def createcluster(self):
      """Create a db cluster."""
      return "hello"

    # @route('/startcluster', method=['POST'])
    # def startcluster(self):
    #     """Start the db cluster we have stopped."""
    #     pass
    #
    # @route('/reinitialize', method=['POST'])
    # def reinitialize(self):
    #     """Start the db cluster we have stopped."""
    #     pass
    #
    # @route('/stopcluster', method=['POST'])
    # def stopcluster(self):
    #     """Stop the db cluster which is running."""
    #     pass
    #
    #
    #
    # @route('/deletecluster', method=['POST'])
    # def deletecluster(self):
    #     """delete the db cluster we have stopped."""
    #     pass
    #
    # @route('/scale', method=['POST'])
    # def addnode(self):
    #     """Add one node to the db cluster."""
    #     pass
    #
    # @route('/stopnode', method=['POST'])
    # def stopnode(self):
    #     """Stop the db node which is running."""
    #     pass
    #
    #
    # @route('/deletenode', method=['POST'])
    # def deletenode(self):
    #     """Deleted the db node we have stopped."""
    #     pass
    #
    # @route('/startnode', method=['POST'])
    # def startnode(self):
    #     """Start the db node we have stopped."""
    #     pass
    #
    # @route('/mysql/resetdata', method=['POST'])
    # def resetdata(self):
    #     """"""
    #     pass

    # @route('/', method=['GET'])
    # def clusters(self):
    #     """Landing page, showing the list of managed clusters."""
    #     return self._clusters_template.render(clusters=self._scheduler.clusters)
    #
    # @route('/nodes', method=['GET'])
    # def nodes(self):
    #     cluster_name = bottle.request.GET.get('cluster_name', default=None)
    #     return self._nodes_template.render(nodes=self._scheduler.nodes, cluster_name=cluster_name)
    #
    # @route('/createservice', method=['GET'])
    # def createservice(self):
    #     return self._create_template.render()

    # @route('/static/<filepath:path>', method=['GET'])
    # def serve_static(self, filepath):
    #     return static_file(filepath, root=self._static_dir, download=True)
    #
    # @route("/clustermessage")
    # def clustermessage(self):
    #     pass
    # @route("/nodemessage")
    # def nodemessage(self):
    #     pass
