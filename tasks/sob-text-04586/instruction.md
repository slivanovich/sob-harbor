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
V-Day: Until the Violence Stops: V-Day: Until the Violence Stops (also known as World VDAY) is a 2003 documentary film directed by Abby Epstein.  It follows events marking 2002 V-Day — a grassroots movement inspired by Eve Ensler's 1996 play "The Vagina Monologues".  The film focuses on V-Day activities in the United States, Kenya, Croatia and the Philippines.

Transmetro: Transmetro is a bus rapid transit system in Guatemala City, Guatemala.  The first line opened on February 3, 2007.  The fleet consists of modern Volvo buses made by Ciferal in Brasil.  The buses have fixed stops and partly run on dedicated lanes, avoiding other traffic.  Both stops and vehicles are guarded by municipal police.  Service began in 2007 with a route between the City Hall (Municipalidad) and a market place at Centra Sur (Southern Transfer Station).  The second route, "Eje Central", started operations on August 14, 2010.  This route serves the central corridor between 6th and 7th Avenue of Zones 1, 4, and 9.

Hard to Explain: "Hard to Explain" is the first single from New York garage rock band The Strokes (their only previously released material was "The Modern Age" EP).  It was released first in the UK and was later released in the US with different album artwork.  (The UK version has a photo of two chairs, one red and one black, facing the camera.  The chairs appear to be in a diner or restaurant of some sort.)  Because this single is the first from their debut LP "Is This It", "Hard to Explain" made the anticipation for the album proper very high, and when "Is This It" did come out it was widely hailed as one of the best of the year.  The B-side of this single, "New York City Cops" was omitted from the US version of the album in the wake of the September 11 attacks on the World Trade Center (the chorus to the song contains the lines "New York City cops/They ain't too smart").

Single Video Theory: Single Video Theory is a music documentary directed by Mark Pellington that follows the making of "Yield", the fifth album by the American alternative rock band Pearl Jam.  It was released first on VHS on August 4, 1998, and then on DVD on November 24, 1998.

The City (1939 film): The City is a pioneering short documentary film from 1939 that contrasts the problems of the contemporary urban environment with the superior social and physical conditions that can be provided in a planned community.  It was directed and photographed by Ralph Steiner and Willard Van Dyke based on a treatment by Lewis Mumford based on an outline by Pare Lorentz.  Aaron Copland wrote the musical score and Morris Carnovsky provided the narration.

Spin It Again! Live in Munich: Spin It Again!  Live in Munich is a live album and video by the Canadian band Saga.  It was recorded in 2012 at the end of their 20/20 tour and celebrates the reunion with original singer Michael Sadler.  It was also the first Saga release featuring their new drummer Mike Thorne.  Besides three songs from "20/20", it includes mainly songs from the first five Saga albums.  The concert was released on different formats by edel records/earMUSIC, including a double CD, DVD (Super Jewel Box packaging) and Blu-Ray.  The video formats also include a twenty-minute tour documentary.  The CD has edited applause between the main set and the encores, but otherwise the performance is identical.  As is typical for Saga shows in Germany, Michael Sadler does some German announcements.  The concert also includes a litte "unplugged" set.  After returning to the stage, Sadler says "What shall I play?" .  He starts on "Images (Chapter 1)", then stops, goes into "No Regrets (Chapter 5)", stops again and finally declares "I got it!"  before launching into "Tired World (Chapter 6)".

Xeko: Xeko is a collectible card game revolving around endangered species.  It was launched on Earthday 2006.  It won the "Creative Child Magazine" 2006 Toy of the Year Award and the National Parenting Center's Seal of Approval in its first year.  Four "Mission" sets have been released.  "Mission: Costa Rica" and "Mission: Madagascar", based on biodiversity hotspots were released first.  "Mission: Indonesia", was released in 2007, with the final release, "Mission: China", was released July 19, 2008.  A total of thirty more missions were planned but never developed.

BlazBlue: Chrono Phantasma: BlazBlue: Chrono Phantasma, released in Japan as BlazBlue: Chronophantasma (ブレイブルー クロノファンタズマ , BureiBurū Kuronofantazuma ) , is a 2-D fighting game developed by Arc System Works.  It is the third game of the Blazblue series, set after the events of "".  The game was originally to be released first as an arcade game in the early fourth quarter of 2012, which was later pushed forward to November 2012.  A PlayStation 3 version of the game was released in Japan on October 24, 2013, while it was released in the United States on March 25, 2014.  Due to limited hardware and disc space the game was not released on the Xbox 360.  An updated version of the game titled BlazBlue: Chrono Phantasma Extend (ブレイブルー クロノファンタズマ エクステンド , BureiBurū: Kuronofantazuma Ekusutendo , BlazBlue: Chronophantasma Extend) , dubbed as BlazBlue: Chrono Phantasma 2.0 (ブレイブルー クロノファンタズマ ２.０ , BureiBurū: Kuronofantazuma 2.0 , BlazBlue: Chronophantasma 2.0) in the Arcade version, was originally released for Arcades in October 2014, and for the PlayStation 3, PlayStation Vita, PlayStation 4, and Xbox One in April 2015.  It was released on June 30, 2015 in North America, with the European region version releasing on October 23, 2015.

Tender (Until the Violence Stops): Tender (formerly Until the Violence Stops) is a London-based charitable organisation that works to prevent domestic violence.  Founded in 2003, Tender delivers educational violence prevention programmes to secondary schools, Pupil Referral Units (PRUs) and youth centres throughout Greater London.

501 Züm Queen: 501 Zum Queen is a rapid transit route in Brampton, Ontario.  The first corridor, which began service on September 20, 2010, runs between the Downtown Brampton Terminal in the west to its easterly terminus at York University in the City of Toronto.  Routes 501 and 501A operate east along Queen Street in Brampton.  Route 501 (full service, every 15 minutes peak, every 20 minutes off-peak, and 30 minutes on weekends) continues along Highway 7 through the City of Vaughan and then south on Jane Street to York University.  Route 501A runs express through Vaughan to York University via Highway 407 during peak periods.  This covers the eastern segment of existing Route 1, and replaces Brampton's portion of the former Route 77 and Route 77A to York University, and the temporary Route 177/177A Highway 7 Express.  Route 501 stops at all Viva Orange stops in Vaughan; running nearly the same frequency as Viva Orange, it covers its entire route except for the segment between York University and Downsview Subway Station that is primarily served by TTC express route 196 every 2–15 minutes.  Route 501A replaces and expands the 77A express branch via Highways 427 and 407.  During rush hours it runs at 15-minute intervals, providing a combined 7.5-minute service between Highway 427 and Downtown Brampton, and limited midday service on Route 501A was introduced in September 2011.  Route 1 continues to operate, providing local service between Mount Pleasant GO station and Highway 50; however, service on that route has been reduced to a 10-minute headway during rush hours, and 20-minute headway at other times of the day.

Question: Which documentary was released first, The City or V-Day: Until the Violence Stops?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_question": {
      "type": "string",
      "description": "The question that prompted the comparison."
    },
    "first_released_documentary_title": {
      "type": "string",
      "description": "The title of the documentary released first."
    },
    "first_released_year": {
      "type": "integer",
      "description": "The year the first documentary was released."
    },
    "second_released_documentary_title": {
      "type": "string",
      "description": "The title of the documentary released second."
    },
    "second_released_year": {
      "type": "integer",
      "description": "The year the second documentary was released."
    }
  },
  "required": [
    "comparison_question",
    "first_released_documentary_title",
    "first_released_year",
    "second_released_documentary_title",
    "second_released_year"
  ],
  "additionalProperties": false
}
