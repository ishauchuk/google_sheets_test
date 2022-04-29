import os

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import creds


def main():
    def get_service_simple():
        return build('sheets', 'v4', developerKey=creds.api_key)

    def get_service_sacc():
        creds_json = os.path.dirname(__file__) + "/creds/credentials.json"
        scopes = ['https://www.googleapis.com/auth/spreadsheets']

        creds_service = ServiceAccountCredentials.from_json_keyfile_name(
            creds_json,
            scopes).authorize(
            httplib2.Http())
        return build('sheets', 'v4', http=creds_service)

    # service = get_service_simple()
    service = get_service_sacc()
    sheet = service.spreadsheets()

    sheet_id = "1Pap_tpnRr2VOU9ecBvGBGJkJXNnzFULTkIIsGfuT1Ew"
    # resp = sheet.values().get(spreadsheetId=sheet_id,
    #                           range="Лист1!A1:A999").execute()
    resp = sheet.values().batchGet(spreadsheetId=sheet_id,
                                   ranges=["Лист1", "Лист2"]).execute()

    print(resp)


if __name__ == '__main__':
    main()
