# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_authentication.py

DESCRIPTION:
    This sample demonstrates how to authenticate to the Text Analytics service.

    There are two supported methods of authentication:
    1) Use a Cognitive Services/Text Analytics API key with AzureKeyCredential from azure.core.credentials
    2) Use a token credential from azure-identity to authenticate with Azure Active Directory

    See more details about authentication here:
    https://docs.microsoft.com/azure/cognitive-services/authentication

USAGE:
    python sample_authentication.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_TEXT_ANALYTICS_ENDPOINT - the endpoint to your Cognitive Services/Text Analytics resource.
    2) AZURE_TEXT_ANALYTICS_KEY - your Text Analytics API key
    3) AZURE_CLIENT_ID - the client ID of your active directory application.
    4) AZURE_TENANT_ID - the tenant ID of your active directory application.
    5) AZURE_CLIENT_SECRET - the secret of your active directory application.
"""

import os


class AuthenticationSample(object):

    def authentication_with_api_key_credential(self):
        print("\n.. authentication_with_api_key_credential")
        # [START create_ta_client_with_key]
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.textanalytics import TextAnalyticsClient
        endpoint = os.getenv("AZURE_TEXT_ANALYTICS_ENDPOINT")
        key = os.getenv("AZURE_TEXT_ANALYTICS_KEY")

        text_analytics_client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))
        # [END create_ta_client_with_key]

        doc = ["I need to take my cat to the veterinarian."]
        result = text_analytics_client.detect_language(doc)

        print("Language detected: {}".format(result[0].primary_language.name))
        print("Confidence score: {}".format(result[0].primary_language.score))

    def authentication_with_azure_active_directory(self):
        """DefaultAzureCredential will use the values from these environment
        variables: AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_CLIENT_SECRET
        """
        print("\n.. authentication_with_api_key_credential")
        # [START create_ta_client_with_aad]
        from azure.ai.textanalytics import TextAnalyticsClient
        from azure.identity import DefaultAzureCredential

        endpoint = os.getenv("AZURE_TEXT_ANALYTICS_ENDPOINT")
        credential = DefaultAzureCredential()

        text_analytics_client = TextAnalyticsClient(endpoint, credential=credential)
        # [END create_ta_client_with_aad]

        doc = ["I need to take my cat to the veterinarian."]
        result = text_analytics_client.detect_language(doc)

        print("Language detected: {}".format(result[0].primary_language.name))
        print("Confidence score: {}".format(result[0].primary_language.score))


if __name__ == '__main__':
    sample = AuthenticationSample()
    sample.authentication_with_api_key_credential()
    sample.authentication_with_azure_active_directory()
