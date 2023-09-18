__all__ = ["AccountsClient"]

from dbacademy.clients.rest.common import ApiContainer


class AccountsClient(ApiContainer):
    from dbacademy.clients.rest.common import ApiClient

    def __init__(self, *, account_id: str, username: str, password: str):
        from dbacademy.dbrest.client import DBAcademyRestClient

        self.endpoint = "https://accounts.cloud.databricks.com"
        self.client = DBAcademyRestClient(endpoint=self.endpoint, user=username, password=password)
        self.account_id = account_id

        from dbacademy.dbrest.accounts.scim import AccountScimClient
        self.scim = AccountScimClient(self.client, account_id=account_id)

        from dbacademy.dbrest.accounts.workspaces import WorkspacesClient
        self.workspaces = WorkspacesClient(self.client, self.account_id)
