import ckan.plugins as p

from ckanext.datavicmain.odp_deleter import helpers


class ODPDeleter(p.SingletonPlugin):
    '''
    A plugin for deleting datasets from an ODP when deleted from an IAR
    '''
    p.implements(p.IPackageController, inherit=True)

    def after_delete(self, context, pkg_dict):
        # For Data.Vic - when a dataset/package is deleted from the IAR
        # we need to subsequently delete it from the public ODP CKAN instance
        helpers.purge_dataset_from_odp(context, pkg_dict)
        pass