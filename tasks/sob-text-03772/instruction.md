{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWQXL: WQXL (1470 kHz \"The Point 100.7 FM and 1470 AM\") is a commercial AM radio station in Columbia, South Carolina.  The station is owned by Glory Communications and operated by Capital City Media.  It airs a talk radio format.  Local hosts are heard in morning and afternoon drive times, with nationally syndicated talk shows heard middays, evenings and late nights.  They include Dave Ramsey, Laura Ingraham, Todd Schnitt, Michael Savage, Doug Stephan and Red Eye Radio.  Most hours begin with ABC Radio News, with local and state news supplied by the South Carolina Radio News Network.\n\nWASR (AM): WASR (1420 kHz) is a commercial AM radio station broadcasting a Talk radio format, with an All-News morning show and Oldies music on weekends.  WASR is licensed to Wolfeboro, New Hampshire, and serves the New Hampshire Lakes Region.  The station is owned by Winnipesaukee Radio Station, LLC and uses programming from Westwood One and the Talk Radio Network with national news from CBS Radio News and Westwood One News.  On March 23, 2015, the station added the Boston-based The Howie Carr Show.  The station also carries Laura Ingraham, Clark Howard, Michael Savage and other nationally syndicated talk shows on weekdays.  Overnight on weekdays, Fox Sports Radio is heard.\n\nJerry Doyle: Jerry Doyle (July 16, 1956 – July 27, 2016) was an American talk radio host, right-libertarian political commentator, television actor and founder of the content platform EpicTimes.  His nationally syndicated talk show, \"The Jerry Doyle Show\", aired throughout the United States on Talk Radio Network.  As an actor, Doyle is known for his role as Michael Garibaldi in the science fiction series \"Babylon 5\" (1994–1998).\n\nWWCO: WWCO (1240 AM) is a radio station licensed in Waterbury, Connecticut, broadcasting a talk radio format.  WWCO is part of a four station simulcast, along with 1470 WMMW, Meriden, 610 WSNG, Torrington and the home base, 1360 WDRC (AM), Hartford.  The four stations use the slogan \"The Talk of Connecticut\" featuring a local morning show and syndicated programs the rest of the day, including Dave Ramsey and Michael Savage.  The station is owned by Connoisseur Media Licenses, LLC and features programming from Fox News Radio, Talk Radio Network and Westwood One.  The station provides a blend of issue-oriented talk, news and information.  It also broadcasts New York Yankees baseball games.\n\nWMMW: WMMW (1470 AM) is a radio station licensed to Meriden, Connecticut.  broadcasting a talk radio format.  WMMW is part of a four station simulcast, along with 610 WSNG, Torrington, 1240 WWCO, Waterbury and the home base, 1360 WDRC (AM), Hartford.  The four stations use the slogan \"The Talk of Connecticut\" featuring a local morning show and syndicated programs the rest of the day, including Dave Ramsey and Michael Savage.  The station is owned by Connoisseur Media Licenses, LLC and features programming from Fox News Radio, Talk Radio Network and Westwood One.  The station provides a blend of issue-oriented talk, news and information.\n\nEd Schultz: Edward Andrew \"Ed\" Schultz (born January 27, 1954) is an American television and radio host, a progressive political commentator and a former sports broadcaster.  Schultz currently hosts a daily primetime weekday show on RT America TV channel based in Washington, D.C., that is part of the RT network.  Schultz has hosted a nationally syndicated podcast, \"Ed Schultz News and Commentary\", since 2015 and a nightly television show, \"News with Ed Schultz\", since 2016.  He was the host of \"The Ed Show\", a weekday news talk program on MSNBC, and \"The Ed Schultz Show\", a talk radio show, nationally syndicated by Dial Global.  The radio show ended on May 23, 2014, and was replaced by a one-hour podcast.\n\nWTMA: WTMA (branded as News Talk 1250 WTMA) is an AM radio station licensed to Charleston, South Carolina with a Talk radio format.  This station operates on 1250 kHz and is under the ownership of Cumulus Media.  WTMA airs a local news and interview morning show hosted by Charlie James.  The rest of the weekday schedule is made up of nationally syndicated talk shows from Cumulus subsidiary Westwood One Networks.  They include Chris Plante, Clark Howard, Michael Savage, Mark Levin, John Batchelor, Red Eye Radio and First Light.  Weekends feature shows on money, health, real estate and gardening, with syndicated shows from Larry Kudlow, Bob Brinker and repeats of weekday shows.  Each hour begins with Westwood One News.\n\nSean Hannity: Sean Patrick Hannity (born December 30, 1961) is an American talk show host, author, and conservative political commentator.  Hannity is the host of \"The Sean Hannity Show\", a nationally syndicated talk radio show.  He also hosts a cable news show, \"Hannity\", on Fox News Channel.\n\nMike Gallagher (political commentator): Mike Gallagher is an American radio host and conservative political commentator.  He is the host of \"The Mike Gallagher Show\", a nationally syndicated radio program that airs throughout the United States on Salem Radio Network and is also a FOX News Channel Contributor and guest host.  According to \"Talkers\" magazine, Gallagher is the sixth most-listened-to radio talk show host in the United States.\n\nMichael Savage: Michael Alan Weiner (born March 31, 1942), better known by his professional name Michael Savage, is an American radio host, author, activist, nutritionist, and conservative political commentator.  He is the host of \"The Savage Nation\", a nationally syndicated talk show that aired on Talk Radio Network across the United States until 2012, and in 2009 was the second most listened-to radio talk show in the country with an audience of over 20 million listeners on 400 stations across the United States.  Since October 23, 2012, Michael Savage has been syndicated by Cumulus Media Networks.  He holds master's degrees from the University of Hawaii in medical botany and medical anthropology, and a Ph.D. from the University of California, Berkeley in nutritional ethnomedicine.  As Michael Weiner, he has written books on nutrition, herbal medicine, and homeopathy; as Michael Savage, he has written four political books that have reached \"The New York Times Best Seller List\".\n\nQuestion: WTMA (branded as News Talk 1250 WTMA) is an AM radio station licensed to Charleston, South Carolina with a Talk radio format, it includes which nationally syndicated talk show, Michael Savage, is an American radio host, author, activist, nutritionist, and conservative political commentator, host of which nationally syndicated talk show?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"station_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"call_sign\": {\n          \"type\": \"string\",\n          \"description\": \"The call sign of the radio station.\"\n        },\n        \"frequency_khz\": {\n          \"type\": \"integer\",\n          \"description\": \"The frequency of the radio station in kHz.\"\n        },\n        \"licensed_location\": {\n          \"type\": \"string\",\n          \"description\": \"The city and state where the station is licensed.\"\n        }\n      },\n      \"required\": [\n        \"call_sign\",\n        \"frequency_khz\",\n        \"licensed_location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"host_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the talk show host.\"\n        },\n        \"description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the host's professions and roles.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"description\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"talk_show_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"show_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the nationally syndicated talk show.\"\n        },\n        \"syndication_network\": {\n          \"type\": \"string\",\n          \"description\": \"The network currently syndicating the talk show.\"\n        },\n        \"syndication_start_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date when the show started being syndicated by the current network.\"\n        }\n      },\n      \"required\": [\n        \"show_name\",\n        \"syndication_network\",\n        \"syndication_start_date\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"station_info\",\n    \"host_info\",\n    \"talk_show_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "station_info": {
        "type": "object",
        "properties": {
          "call_sign": {
            "type": "string",
            "description": "The call sign of the radio station."
          },
          "frequency_khz": {
            "type": "integer",
            "description": "The frequency of the radio station in kHz."
          },
          "licensed_location": {
            "type": "string",
            "description": "The city and state where the station is licensed."
          }
        },
        "required": [
          "call_sign",
          "frequency_khz",
          "licensed_location"
        ],
        "additionalProperties": false
      },
      "host_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the talk show host."
          },
          "description": {
            "type": "string",
            "description": "A description of the host's professions and roles."
          }
        },
        "required": [
          "name",
          "description"
        ],
        "additionalProperties": false
      },
      "talk_show_details": {
        "type": "object",
        "properties": {
          "show_name": {
            "type": "string",
            "description": "The name of the nationally syndicated talk show."
          },
          "syndication_network": {
            "type": "string",
            "description": "The network currently syndicating the talk show."
          },
          "syndication_start_date": {
            "type": "string",
            "description": "The date when the show started being syndicated by the current network."
          }
        },
        "required": [
          "show_name",
          "syndication_network",
          "syndication_start_date"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "station_info",
      "host_info",
      "talk_show_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
