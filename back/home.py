import sys
import json
from google.protobuf.json_format import Parse
from google.protobuf.json_format import ParseDict
import flashback_home_pb2  # for home (activities)
data = {
        "kind": "youtube#activityListResponse",
        "etag": "xFEh_4ty-ENBH3JcjuGyK9V4Mkg",
        "items": [
            {
                "kind": "youtube#activity",
                "etag": "Pq3uebmSIX3qA8JrEpPbHqgJpiM",
                "id": "MTUxNjU5MTI1OTgxMTY1OTEyNTk4MTAwMDc0Mg",
                "snippet": {
                    "publishedAt": "2022-07-29T20:19:41+00:00",
                    "channelId": "UCzaZDxXdHRkUaZn6Xaw2NwA",
                    "title": "MACringe",
                    "description": "bruh",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/BxH6QFWiSE4/default.jpg",
                            "width": 120,
                            "height": 90
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/BxH6QFWiSE4/mqdefault.jpg",
                            "width": 320,
                            "height": 180
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/BxH6QFWiSE4/hqdefault.jpg",
                            "width": 480,
                            "height": 360
                        },
                        "standard": {
                            "url": "https://i.ytimg.com/vi/BxH6QFWiSE4/sddefault.jpg",
                            "width": 640,
                            "height": 480
                        },
                        "maxres": {
                            "url": "https://i.ytimg.com/vi/BxH6QFWiSE4/maxresdefault.jpg",
                            "width": 1280,
                            "height": 720
                        }
                    },
                    "channelTitle": "Brn",
                    "type": "upload"
                },
                "contentDetails": {
                    "upload": {
                        "videoId": "BxH6QFWiSE4"
                    }
                }
            },
            {
                "kind": "youtube#activity",
                "etag": "q5UfMGTWe5HoEZg4a0Z35SlRAUQ",
                "id": "MTUxNjM5MzMzOTUyMTYzOTMzMzk1MjAwMDYxNA",
                "snippet": {
                    "publishedAt": "2021-12-12T18:32:32+00:00",
                    "channelId": "UCzaZDxXdHRkUaZn6Xaw2NwA",
                    "title": "English Presentation, TV Shows",
                    "description": "",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/p9-GUi7UOCY/default.jpg",
                            "width": 120,
                            "height": 90
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/p9-GUi7UOCY/mqdefault.jpg",
                            "width": 320,
                            "height": 180
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/p9-GUi7UOCY/hqdefault.jpg",
                            "width": 480,
                            "height": 360
                        },
                        "standard": {
                            "url": "https://i.ytimg.com/vi/p9-GUi7UOCY/sddefault.jpg",
                            "width": 640,
                            "height": 480
                        },
                        "maxres": {
                            "url": "https://i.ytimg.com/vi/p9-GUi7UOCY/maxresdefault.jpg",
                            "width": 1280,
                            "height": 720
                        }
                    },
                    "channelTitle": "Brn",
                    "type": "upload"
                },
                "contentDetails": {
                    "upload": {
                        "videoId": "p9-GUi7UOCY"
                    }
                }
            }
        ],
        "pageInfo": {
            "totalResults": 2,
            "resultsPerPage": 18
        }
    }
def process_request(data):
    # creating a protobuf top level instance
    activity_list_response = flashback_home_pb2.ActivityListResponse()
    # Parse the JSON dictionary into the protobuf message
    ParseDict(data, activity_list_response)
    return activity_list_response

if __name__ == "__main__":
    try:
        input_data = sys.stdin.read()
        #request_data = json.loads(input_data)
        response_data = process_request(data)
        sys.stdout.buffer.write(response_data.SerializeToString())
    except json.JSONDecodeError:
        print(json.dumps({"error": "Invalid JSON input"}, indent=2))
    except Exception as e:
        print(json.dumps({"errorza": str(e)}, indent=2))