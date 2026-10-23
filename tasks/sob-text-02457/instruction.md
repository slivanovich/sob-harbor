{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJapanese invasion of Taiwan (1895): The Japanese invasion of Taiwan () (May–October 1895) was a conflict between the Empire of Japan and the armed forces of the short-lived Republic of Formosa following the Qing Dynasty's cession of Taiwan to Japan in April 1895 at the end of the First Sino-Japanese War.  The Japanese sought to take control of their new possession, while the Republican forces fought to resist Japanese occupation.  The Japanese landed near Keelung on the northern coast of Taiwan on 29 May 1895, and in a five-month campaign swept southwards to Tainan.  Although their advance was slowed by guerrilla activity, the Japanese defeated the Formosan forces (a mixture of regular Chinese units and local Hakka militias) whenever they attempted to make a stand.  The Japanese victory at Baguashan on 27 August, the largest battle ever fought on Taiwanese soil, doomed the Formosan resistance to an early defeat.  The fall of Tainan on 21 October ended organised resistance to Japanese occupation, and inaugurated five decades of Japanese rule in Taiwan.\n\nLopezia: Lopezia is a genus of plants of the family Onagraceae, largely restricted to Mexico.\n\nFatsia japonica: Fatsia japonica(syn.  \"Aralia japonica\" Thunb. , \"A. sieboldii\" Hort.  ex K.Koch), also glossy-leaf paper plant, fatsi, paperplant or Japanese aralia, is a species of flowering plant in the family Araliaceae, native to southern Japan, southern Korea, and Taiwan.\n\nFatsia: Fatsia is a small genus of three species of evergreen shrubs native to southern Japan and Taiwan.  They typically have stout, sparsely branched stems bearing spirally-arranged, large leathery, palmately lobed leaves 20–50 cm in width, on a petiole up to 50 cm long, and small creamy-white flowers in dense terminal compound umbels in late autumn or early winter, followed by small black fruit.\n\nTetrapanax: Tetrapanax papyrifer (rice-paper plant, or \"通草—tong cao\") is an evergreen shrub in the family Araliaceae, the sole species in the genus Tetrapanax.  The specific epithet is frequently misspelled as \"papyriferum\", \"papyriferus\", or \"papyrifera\".  It is endemic to Taiwan, but widely cultivated in East Asia and sometimes in other tropical regions as well.  The species was once included in the genus \"Fatsia\" as \"Fatsia papyrifera\".\n\nFatsia polycarpa: Fatsia polycarpa is a species of plant in the Araliaceae family.  It is endemic to Taiwan.  It is threatened by habitat loss.\n\nJapanese invasion of Taiwan (1874): The Japanese punitive expedition to Taiwan in 1874, referred to in Japan as the Taiwan Expedition (Japanese: 台湾出兵 , Hepburn: Taiwan Shuppei ) and in Taiwan and mainland China as the Mudan incident (), was a punitive expedition launched by the Japanese in retaliation for the murder of 54 Ryukyuan sailors by Paiwan aborigines near the southwestern tip of Taiwan in December 1871.  The success of the expedition, which marked the first overseas deployment of the Imperial Japanese Army and Imperial Japanese Navy, revealed the fragility of the Qing dynasty's hold on Taiwan and encouraged further Japanese adventurism.  Diplomatically, Japan's embroilment with China in 1874 was eventually resolved by a British arbitration under which Qing China agreed to compensate Japan for property damage.  Some ambiguous wording in the agreed terms were later argued by Japan to be confirmation of Chinese renunciation of suzerainty over the Ryukyu Islands, paving the way for \"de facto\" Japanese incorporation of Ryukyu in 1879.\n\nCastle (Jolin Tsai album): Castle ( ) is the sixth studio album by Taiwanese singer Jolin Tsai ( ).  It was released on February 27, 2004, by Sony Music Taiwan.  Following the success of her last studio album, \"Magic\" (2003), Tsai continued to secure her A-list status with the new release.  Tsai again rang up huge sales with the album, which further increased her popularity in her native Taiwan as well as in other Asian countries.  The album has sold more than 2 million copies in Asia, with more than 300,000 copies sold in Taiwan alone, and made her the best-selling female singer of the year in Taiwan.  The second track, \"It's Love\", reached number 8 on the Hit FM Top 100 Singles of the Year.  The opening track, \"36 Tricks of Love\", reached number 78 on the chart.  The album earned Tsai an MTV Asia Award nomination for Favorite Artist Taiwan.  The music video of the lead single, \"Pirates\", earned Tsai an MTV Video Music Award Japan nomination for Best Buzz Asia.\n\nTaiwan under Qing rule: Taiwan under Qing rule refers to the rule of the Qing dynasty over Formosa (modern-day Taiwan) and the Pescadores (Penghu) from 1683 to 1895.  The Qing court sent an army led by general Shi Lang and annexed Taiwan in 1683.  It was governed as Taiwan Prefecture of Fujian Province until the declaration of Fujian-Taiwan Province in 1887.  Qing rule over Taiwan ended when Taiwan was ceded to Japan by the Treaty of Shimonoseki in 1895.\n\nTaiwan studies: Taiwan studies is a multi-disciplinary academic division of area studies (a part of East Asian studies) focused on studying Taiwan and the people on/in/of Taiwan both on its own and in comparison with other world areas.  Academia Sinica, Taiwan's national level research institute, officially inaugurated its Institute of Taiwan History in 2004 following a long exploratory period beginning in 1986.  Taiwan studies departments and centers have been established in numerous universities around the world (see below for a list) and key Taiwan studies organizations have been established in North America (NATSA), Europe (EATS), and Japan (JATS).  The first \"World Congress of Taiwan Studies (WCTS)\" was hosted by Taiwan's Academia Sinica on April 26–28, 2012, in Taipei, Taiwan.  More recently, the People's Republic of China has begun to establish its own controversial version of Taiwan studies in the United States via its Confucius Institutes.\n\nQuestion: Which of the following is native to Japan and Taiwan: Lopezia or Fatsia?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"plant_identified\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the plant identified as native to both Japan and Taiwan.\"\n        },\n        \"is_native_to_japan_and_taiwan\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if this plant is native to both Japan and Taiwan.\"\n        },\n        \"native_regions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of regions where this plant is native according to the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"is_native_to_japan_and_taiwan\",\n        \"native_regions\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"other_plant_mentioned\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the other plant mentioned in the question.\"\n        },\n        \"is_native_to_japan_and_taiwan\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if this plant is native to both Japan and Taiwan.\"\n        },\n        \"native_regions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of regions where this plant is native according to the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"is_native_to_japan_and_taiwan\",\n        \"native_regions\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer_summary\": {\n      \"type\": \"string\",\n      \"description\": \"A summary statement answering the question.\"\n    }\n  },\n  \"required\": [\n    \"plant_identified\",\n    \"other_plant_mentioned\",\n    \"answer_summary\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "plant_identified": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the plant identified as native to both Japan and Taiwan."
          },
          "is_native_to_japan_and_taiwan": {
            "type": "boolean",
            "description": "Indicates if this plant is native to both Japan and Taiwan."
          },
          "native_regions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of regions where this plant is native according to the context."
          }
        },
        "required": [
          "name",
          "is_native_to_japan_and_taiwan",
          "native_regions"
        ],
        "additionalProperties": false
      },
      "other_plant_mentioned": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the other plant mentioned in the question."
          },
          "is_native_to_japan_and_taiwan": {
            "type": "boolean",
            "description": "Indicates if this plant is native to both Japan and Taiwan."
          },
          "native_regions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of regions where this plant is native according to the context."
          }
        },
        "required": [
          "name",
          "is_native_to_japan_and_taiwan",
          "native_regions"
        ],
        "additionalProperties": false
      },
      "answer_summary": {
        "type": "string",
        "description": "A summary statement answering the question."
      }
    },
    "required": [
      "plant_identified",
      "other_plant_mentioned",
      "answer_summary"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
