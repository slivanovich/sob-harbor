Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
2014 Iquique earthquake: The 2014 Iquique earthquake struck off the coast of Chile on 1 April, with a moment magnitude of 8.2, at 20:46 local time (23:46 UTC).  The epicenter of the earthquake was approximately 95 km northwest of Iquique.  The mainshock was preceded by a number of moderate to large shocks and was followed by a large number of moderate to very large aftershocks, including a M7.7 event on 3 April.  The megathrust earthquake triggered a tsunami of up to 2.11 m that hit Iquique at 21:05 local time (00:05 UTC, 2 April).  Similar-sized tsunamis were also reported to have hit the coasts of Pisagua and Arica.

2012 Chiba earthquake: The 2012 Chiba earthquake (千葉県東方沖地震 , Chiba-ken Toho-oki Jishin , lit.  "Offshore Eastern Chiba Earthquake") occurred along the northeastern coast of Chiba Prefecture, Japan at 21:05 JST (12:05 UTC) on Wednesday, 14 March.  Although its epicentre lay just offshore near Chōshi city, the shallow magnitude 6.1 M earthquake produced considerable shaking inland through much of the Bōsō Peninsula and lower Ibaraki Prefecture.  It occurred as a result of normal faulting in a seismically quiet region, possibly in response to the magnitude 9.0 M 2011 Tōhoku earthquake.

List of earthquakes in 1952: This is a list of earthquakes in 1952.  Only magnitude 6.0 or greater earthquakes appear on the list.  Lower magnitude events are included if they have caused death, injury or damage.  Events which occurred in remote areas will be excluded from the list as they wouldn't have generated significant media interest.  All dates are listed according to UTC time.  Two events dominated 1952 in seismic terms.  Firstly in March a magnitude 8.1 earthquake struck Japan resulting in a robust aftershock sequence.  Then in November, a magnitude 9.0 earthquake rocked the Kamchatka area of Russia.  This event was the largest and deadliest of the year.  The Kamchatka quake was not only the largest of 1952, but also one of the largest of all time.

1983 Sea of Japan earthquake: The 1983 Sea of Japan earthquake or 1983 Nihonkai-Chubu earthquake occurred on May 26, at 11:59:57 local time (02:59:59.6 UTC), It had a magnitude of 7.8 on the moment magnitude scale.  It occurred in the Sea of Japan, about 100 km west of the coast of Noshiro in Akita Prefecture, Japan.  Out of the 104 fatalities, all but four were killed by the resulting tsunami, which struck communities along the coast, especially Aomori and Akita Prefectures and the east coast of Noto Peninsula.  Images of the tsunami hitting the fishing harbor of Wajima on Noto Peninsula was broadcast on TV.  The waves exceeded 10 m in some areas.  Three of the fatalities were along the east coast of South Korea (whether North Korea was affected is not known).  The tsunami also hit Okushiri Island, the site of a more deadly tsunami 10 years later.

April 2011 Miyagi earthquake: The April 2011 Miyagi earthquake (Japanese: "2011 Miyagi Prefecture earthquake" (2011年 宮城県沖地震 , 2011-Nen Miyagi-ken-oki jishin ) ) was a magnitude 7.1 M earthquake, with an epicentre off the coast of Miyagi Prefecture, approximately 66 km east of Sendai, Japan.  The earthquake was classified as an aftershock of the March 11 Tōhoku earthquake, and occurred at 23:32 JST (14:32 UTC) on Thursday, 7 April 2011.

869 Sanriku earthquake: The 869 Sanriku earthquake (貞観地震 , Jōgan jishin ) and associated tsunami struck the area around Sendai in the northern part of Honshu on 9 July (26th day of 5th month, 11th year of Jōgan).  The earthquake had an estimated magnitude of at least 8.4 on the moment magnitude scale, but may have been as high as 9.0, similar to the 2011 Tōhoku earthquake and tsunami.  The tsunami caused widespread flooding of the Sendai plain, with sand deposits being found up to 4 km from the coast.

2011 Tōhoku earthquake and tsunami: The 2011 earthquake off the Pacific coast of Tōhoku (東北地方太平洋沖地震 , Tōhoku-chihō Taiheiyō Oki Jishin ) was a magnitude 9.0–9.1 (M) undersea megathrust earthquake off the coast of Japan that occurred at 14:46 JST (05:46 UTC) on Friday 11 March 2011, with the epicentre approximately 70 km east of the Oshika Peninsula of Tōhoku and the hypocenter at an underwater depth of approximately 29 km .  The earthquake is often referred to in Japan as the Great East Japan Earthquake (東日本大震災 , Higashi nihon daishinsai ) and is also known as the 2011 Tōhoku earthquake, and the 3.11 earthquake.  It was the most powerful earthquake ever recorded in Japan, and the fourth most powerful earthquake in the world since modern record-keeping began in 1900.  The earthquake triggered powerful tsunami waves that reached heights of up to 40.5 m in Miyako in Tōhoku's Iwate Prefecture, and which, in the Sendai area, traveled up to 10 km inland.  The earthquake moved Honshu (the main island of Japan) 2.4 m east, shifted the Earth on its axis by estimates of between 10 cm and 25 cm , and generated infrasound waves detected in perturbations of the low-orbiting GOCE satellite.

2004 Indian Ocean earthquake and tsunami: The 2004 Indian Ocean earthquake occurred at 00:58:53 UTC on 26 December with the epicentre off the west coast of Sumatra, Indonesia.  The shock had a moment magnitude of 9.1–9.3 and a maximum Mercalli intensity of IX ("Violent").  The undersea megathrust earthquake was caused when the Indian Plate was subducted by the Burma Plate and triggered a series of devastating tsunamis along the coasts of most landmasses bordering the Indian Ocean, killing 230,000–280,000 people in 14 countries, and inundating coastal communities with waves up to 30 m high.  It was one of the deadliest natural disasters in recorded history.  Indonesia was the hardest-hit country, followed by Sri Lanka, India, and Thailand.

No.18 Kyotoku-maru: Kyotoku-maru no. 18 is a fishing trawler which was swept inland during tsunami that followed the 2011 Tōhoku earthquake and tsunami, in the city of Kesennuma, Miyagi in Japan.

April 2011 Fukushima earthquake: The April 2011 Fukushima earthquake (福島県浜通り地震 , Fukushima-ken Hamadōri jishin ) was a potent magnitude 6.6 M intraplate aftershock that occurred at 17:16 JST (08:16 UTC) on 11 April in the Hamadōri region of Fukushima, Japan.  With a shallow focus of 13 km , the earthquake was centred inland about 36 km west of Iwaki, causing widespread strong to locally severe shaking.  It was one of many aftershocks to follow the 11 March Tōhoku earthquake, and the strongest to have its epicentre located inland.

Question: Kyotoku-maru no. 18 is a fishing trawler which was swept inland during tsunami that followed which titled event, that was a magnitude 9.0–9.1 (M) undersea megathrust earthquake off the coast of Japan that occurred at 14:46 JST (05:46 UTC) on Friday 11 March 2011, with the epicentre approximately 70 km east of the Oshika Peninsula of Tōhoku and the hypocenter at an underwater depth of approximately 29 km?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "earthquake_event_name": {
      "type": "string",
      "description": "The official title or name of the earthquake event."
    },
    "magnitude": {
      "type": "string",
      "description": "The moment magnitude of the earthquake."
    },
    "event_type": {
      "type": "string",
      "description": "The geological classification or type of the earthquake."
    },
    "location_description": {
      "type": "string",
      "description": "A description of the earthquake's general location."
    },
    "event_date_utc": {
      "type": "string",
      "format": "date",
      "description": "The date of the earthquake in UTC."
    },
    "event_time_utc": {
      "type": "string",
      "format": "time",
      "description": "The time of the earthquake in UTC."
    },
    "epicenter_details": {
      "type": "object",
      "properties": {
        "distance_from_landmark_km": {
          "type": "integer",
          "description": "Distance of the epicenter from a known landmark in kilometers."
        },
        "landmark_name": {
          "type": "string",
          "description": "The name of the landmark relative to the epicenter."
        },
        "direction_from_landmark": {
          "type": "string",
          "description": "The direction of the epicenter from the landmark (e.g., 'east of')."
        }
      },
      "required": [
        "distance_from_landmark_km",
        "landmark_name",
        "direction_from_landmark"
      ],
      "additionalProperties": false
    },
    "hypocenter_depth_km": {
      "type": "integer",
      "description": "The underwater depth of the hypocenter in kilometers."
    },
    "affected_vessel": {
      "type": "object",
      "properties": {
        "vessel_name": {
          "type": "string",
          "description": "The name of the vessel affected by the tsunami."
        },
        "vessel_type": {
          "type": "string",
          "description": "The type of the vessel."
        },
        "impact_description": {
          "type": "string",
          "description": "How the vessel was affected by the tsunami."
        }
      },
      "required": [
        "vessel_name",
        "vessel_type",
        "impact_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "earthquake_event_name",
    "magnitude",
    "event_type",
    "location_description",
    "event_date_utc",
    "event_time_utc",
    "epicenter_details",
    "hypocenter_depth_km",
    "affected_vessel"
  ],
  "additionalProperties": false
}
