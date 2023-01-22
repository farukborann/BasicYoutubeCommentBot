import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = r"C:\Users\USER\Desktop\DENEME EXCEL\youtube\96mercan.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    videos = pd.read_excel(r"C:\Users\USER\Desktop\DENEME EXCEL\youtube\test.xlsx")
    commentThreads = youtube.commentThreads()

    for index, row in videos.iterrows():
      try:
        request = commentThreads.insert(
          part="snippet",
          body={
            "snippet": {
              "videoId": row["id"],
              "topLevelComment": {
                "snippet": {
                  "textOriginal": row["comment"]
                }
              }
            }
          }
        )
        request.execute()
        print(row["link"], " => ", row["comment"])
      except:
        print("Yorum yapılamadı !!! => ", row["link"], " => ", row["comment"])



if __name__ == "__main__":
    main()