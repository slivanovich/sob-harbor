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
Jim Brough: James Wasdale Brough (5 November 1903 – 16 September 1986) was an English dual-code international rugby union and professional rugby league footballer who played in the 1920s, and 1930s, and coached rugby league in the 1950s, playing representative level rugby union (RU) for England, and Cumberland, and at club level for Silloth RUFC, as a fullback, and playing representative level rugby league for Great Britain (Captain), and England, and at club level for Leeds, as a fullback , or centre , and coaching representative level rugby league for Great Britain, and at club level for Workington Town.  He died in Workington, Cumbria.

Dai Prosser: David "Dai" Rees Prosser (13 October 1912 – 6 May 1973 (aged 60)) born in Neath, was a Welsh dual-code international rugby union and professional rugby league footballer who played in the 1930s, and 1940s, and coached rugby league in the 1960s, playing representative level rugby union (RU) for Wales, and Glamorgan County RFC, and at club level for Glynneath RFC, Neath RFC, and Swansea RFC, as a Prop forward, i.e. number 1 or 3, and playing representative level rugby league (RL) for Great Britain, and Wales, and at club level for York, and Leeds, as a prop , i.e. number 8 or 10, during the era of contested scrums, and coaching club level rugby league for Leeds.  Dai Prosser was a Bombardier in the British Army during World War II, he died in York.

Kevin Ashcroft: Kevin Ashcroft is a professional rugby league footballer who played in the 1960s, and 1970s, and coached in the 1970s, 1980s, and 1990s, playing at representative level for Great Britain, and Lancashire, and at club level for Rochdale Hornets, Dewsbury, Leigh, Warrington and Salford, as a prop , or hooker , i.e. number 8 or 10, or, 9, during the era of contested scrums, and coaching at club level for Leigh (twice), and Salford.  Ashcroft is a Warrington Hall of Fame inductee.

Tony Fisher (rugby): Anthony "Tony" Fisher is a Welsh rugby union and professional rugby league footballer who played in the 1960s, and 1970s, and coached rugby league in the 1980s, and 1990s, playing club level rugby union (RU) for Swansea RFC, as a Hooker, and playing representative level rugby league (RL) for Great Britain and Wales national, and at club level for Bradford Northern (twice), Leeds, and Castleford, as a prop , or hooker , i.e. number 8 or 10, or 9, during the era of contested scrums, and coaching representative level rugby league (RL) for South Africa, and at club level for Bramley, Keighley, Doncaster, and Dewsbury.

Les Sheard: Leslie Sheard is an English school teacher, and rugby union and professional rugby league footballer who played in the 1970s, and 1980s, and coached in the 1980s, playing club level rugby union (RU) for Wakefield RFC, and playing representative level rugby league (RL) for England, and Yorkshire, and at club level for Castleford, Wakefield Trinity (Heritage № 777), York (captain), and Huddersfield, as a fullback , or centre , i.e. number 1, or, 2 or 5, and coaching club level rugby league (RL) for Huddersfield, as of 2009 he lives in Devon. <ref name="York Rugby League Club’s championship-winning team of 1980/1 to be re-united at a special dinner"> </ref>

Matthew Silva: Matthew Silva (born 15 March 1970 in Tremorfa, Cardiff) is a Welsh rugby union and professional rugby league footballer who played in the 1980s, 1990s, and 2000s, and current rugby union coach, playing club level rugby union (RU) for St Albans RFC (Cardiff), Llandaff RFC, Newport RFC, Pontypool RFC, Newbridge RFC, West Hartlepool R.F.C., Cardiff RFC, Treorchy RFC, Rumney RFC, and Llantwit Major RFC, as a Number Eight, Fly-half, Centre, Wing, Fullback, and playing representative level rugby league (RL) for Wales, and at club level for Halifax, as a fullback , i.e. number 1, and coaching club level rugby union (RU) for Llantwit Major RFC, Beddau RFC, Cardiff RFC, and Rumney RFC, and Cardiff Blues Under-16, Under-18, and Under-20 and Bridgend Ravens RFC, from 2005 to 2013 he was the Welsh Rugby Union/Cardiff Blues Player Development Officer for the Vale of Glamorgan.  From 2013 to 2015 he was Director of Rugby at Cowbridge Comprehensive School and was responsible for establishing the Rugby Academy that competes in the Welsh Rugby Union National Colleges League.  In 2015 he became the Welsh Rugby Union and Ospreys Coach Development Officer.

Warrington Wolves: Warrington Wolves R.L.F.C. is a professional rugby league football club based in Warrington, England that competes in Super League.  They play at the Halliwell Jones Stadium, having moved there from Wilderspool in 2003.

Colin Dixon: Colin J. "Dicko" Dixon (3 December 1943 – 21 June 1993) born in Butetown, was a Welsh rugby union and professional Rugby League World Cup winning footballer who played in the 1960s, 1970s, and 1980s, and rugby league coached in the 1970s, playing club level rugby union (RU) for Cardiff International Athletic Club, and playing representative level rugby league (RL) for Great Britain, and Wales, and at club level for Halifax (captain), Salford, and Hull Kingston Rovers, as a centre , or loose forward/lock , i.e. number 3 or 4, 11 or 12, or 13, and coaching club level rugby league (RL) for Salford, he is a Halifax Hall of Fame Inductee, he died in Halifax, West Yorkshire.

Neil Kelly: Neil Kelly (born Thursday (1962--) 10 1962 (age (2017)-(1962)-((11)<(05)or(11)==(05)and(29)<(10)) ) in Wakefield) is an English professional rugby league footballer who played in the 1980s, and 1990s, and internationally qualified rugby league and rugby union coach, playing club level rugby league (RL) for Dewsbury Rams (twice), Featherstone Rovers, Wakefield Trinity, and Hunslet Hawks as a hooker or loose forward/lock , and coaching representative level rugby league (RL) for Wales, and at club level for Dewsbury Rams, Widnes Vikings, Leigh Centurions, and coaching representative level rugby union (RU) for Namibia (assistant), and at club level for Ulster Rugby (defence), and Doncaster Knights (assistant).

Colin Greenwood (rugby): Colin "Col" Marius Greenwood (25 January 1936 in Cape Town, Western Cape, South Africa – 3 October 1998) was a South African dual-code international rugby union and professional rugby league footballer who played in the 1960s, and coached in the 1960s, playing representative level rugby union (RU) for South Africa, at provincial level for Western Province, and at club level for Noordelikes (Northerns), as a Centre, i.e. number 12 or 13, and playing representative level rugby league (RL) for South Africa, and Rugby League XIII, and at club level for Wakefield Trinity (Heritage № 674), North Sydney Bears, and Canterbury-Bankstown Bulldogs, as a wing , stand-off/five-eighth , or lock/loose forward , i.e. number 2 or 5, 6, or 13 and coaching club level rugby league (RL) for North Sydney Bears, he died in George, Western Cape, South Africa.

Question: Kevin Ashcroft has played at club level for the rugby league club that competes in what stadium?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the rugby player."
    },
    "club_played_for": {
      "type": "string",
      "description": "The name of the club the player played for that is associated with a stadium."
    },
    "stadium_name": {
      "type": "string",
      "description": "The name of the stadium where the identified club competes."
    },
    "sport_type": {
      "type": "string",
      "description": "The type of sport played by the club."
    }
  },
  "required": [
    "player_name",
    "club_played_for",
    "stadium_name",
    "sport_type"
  ],
  "additionalProperties": false
}
