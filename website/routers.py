import random
 
class MasterSlaveRouter(object):
    
      route_app_labels = {'users', 'restaurant'}

      def db_for_read(self, model, **hints):
            """
            Reads go to a randomly-chosen slave.
            """
            if model._meta.app_label in self.route_app_labels:
                  return random.choice(['slave1', 'slave2'])
            return None
            # return random.choice(['slave1', 'slave2'])
      
      def db_for_write(self, model, **hints):
            """
            Writes always go to defautl.
            """
            if model._meta.app_label in self.route_app_labels:
                  return 'default'
            return None
            # return 'defautl'
      
      def allow_relation(self, obj1, obj2, **hints):
            """
            Relations between objects are allowed if both objects are
            in the master/slave pool.
            """
            # route_app_labels = ('defautl', 'slave1', 'slave2')
            if (
                  obj1._meta.app_label in self.route_app_labels
                  or obj2._meta.app_label in self.route_app_labels
            ):
                  return True
            return None
      
      def allow_syncdb(self, db, model):
            """
            All non-auth models end up in this pool.
            """
            return True
      
      