from __future__ import print_function, absolute_import, unicode_literals
from prompt_toolkit.formatted_text import HTML

class Toolbar(object):
    """Show information about the kube-shell in a tool bar.

    :type handler: callable
    :param handler: Wraps the callable `get_toolbar_items`.

    """

    def __init__(self, get_cluster_name, get_namespace, get_user, get_inline_help):
        self.handler = self._create_toolbar_handler(get_cluster_name, get_namespace, get_user, get_inline_help)

    def _create_toolbar_handler(self, get_cluster_name, get_namespace, get_user, get_inline_help):
        def get_toolbar_items():
            if get_inline_help():
                help_text = "ON"
            else:
                help_text = "OFF"

            cluster_name = get_cluster_name() or "unknown"
            namespace = get_namespace() or "default"
            user = get_user() or "unknown"

            return HTML(
                '<b>[F4] Cluster:</b> {cluster} '
                '<b>[F5] Namespace:</b> {namespace} '
                '<b>User:</b> {user} '
                '<b>[F9] In-line help:</b> {help} '
                '<b>[F10] Exit</b>'.format(
                    cluster=cluster_name,
                    namespace=namespace,
                    user=user,
                    help=help_text
                )
            )

        return get_toolbar_items
