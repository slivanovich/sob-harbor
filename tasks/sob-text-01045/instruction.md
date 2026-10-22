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
Saman Piyasiri Fernando: Saman Piyasiri Fernando (also known as Keerthi Vijayabahu; died December 29, 1989), was the military wing leader of the Janatha Vimukthi Peramuna during the 1987-89 insurrection in Sri Lanka, the JVP's military wing also known as "Deshapremi Janatha Viyaparaya" (DJV).  Saman Piyasiri a graduate of the University of Kelaniya, Sri Lanka later joined the JVP and promoted to the higher ranks of the party, appointed as the militarty wing leader and finally led the party after the death of the founding leader Rohana Wijeweera.

Cand.theol.: Candidatus theologiæ (male), Candidata theologiæ (female), abbreviated cand.  theol.  is an academic degree with a long tradition, awarded after a six-year higher education in theology in Iceland, Denmark, and Norway.  In Norway, the title has remained after the "Quality Reform".  In Denmark the title is described as equivalent to Master of Theology, while in Norway it ranks higher.

Academic ranks in Argentina: Professors are usually categorized as "ordinario" or "concursado" (tenured, selected by a jury composed of tenured professors or other reputed authorities on the subject, after a selection process involving academic background evaluation and a public dissertation), "interino" (non-tenure, but stable position, the professor is proposed by the director of the corresponding department – sometimes after different selection processes – and accepted by the Consejo Directivo of the corresponding school), or "suplente" (substitute, hired through the same process as interinos).  In most cases, classes are taught by a professorial team (a "cátedra", chair), formed by one or two professors and auxiliars, which generally also functions as a research team.  Regardless of the rank, professors in public universities (and in many private ones) must perform research.  This ranking system is the one used at the Universidad de Buenos Aires (the largest Argentine university) and by most of the public universities, but not all of them; being autonomous, they can choose their own scale.  Private universities have their own rank in each case, sometimes based on the public university system, although as a general rule they have less ranks or hold a higher ranking as the starting point for a teaching career (devoting auxiliar ranks to undergraduates).

Science and technology in Israel: Science and technology in Israel is one of the country's most developed sectors.  Israel spent 4.2% of its gross domestic product (GDP) on civil research and development in 2013, one of the highest ratios in the world.  Israel ranks fifth among the most innovative countries in the Bloomberg Innovation Index.  It ranks thirteenth in the world for scientific output as measured by the number of scientific publications per million citizens.  In 2014, Israel's share of scientific articles published worldwide (0.9%) was much higher than its share of the global population (0.1%).  It also has one of the highest per capita rates of filed patents.

Lewis Wing: Lewis Wing (born 23 June 1995) is an English professional footballer who plays for EFL Championship club Middlesbrough, as an attacking midfielder.

Lewis Mills (rugby league): Lewis Mills (born 30 May 1989 in Cardiff) is a Wales international rugby league footballer who currently plays for Crusaders in the European Super League and is dual registered with the South Wales Scorpions in the Championship 1.  He signed for the Crusaders, then Celtic Crusaders in 2008, after coming through the youth ranks at Newport Titans.  Mills' position of preference is prop-forward.  Mills made his Super League début in 2009's Super League XIV, coming off the bench in a round 24 loss away to Wakefield Trinity Wildcats.  He has since played one three more occasions, all of which were substitute appearances.  Mills also gained national honours, playing for his native Wales in their European Cup success in 2009.

Football in Colombia: Football is the most popular sport in Colombia (according to FIFA, there are 3,043,229 players total, 291,229 of which are registered and 2,752,000 are unregistered; with 2,773 clubs and 15,800 officials).  The Colombian national league ranks 9th in the IFFHS's ranking "The Strongest National League in the World" of 2014 (3rd in South America).

Order of the Paulownia Flowers: The Order of the Paulownia Flowers (桐花章 , Tōka shō ) is an order presented by the Japanese government.  Established in 1888 during the Meiji Restoration as the highest award in the Order of the Rising Sun; however, since 2003 it has been an Order in its own right.  The only grade of the order is "Grand Cordon of the Order of the Paulownia Flowers" (旭日桐花大綬章 , Kyokujitsu tōka daijushō ) , which ranks higher than the Order of the Rising Sun but lower than the Order of the Chrysanthemum.

EFL Championship: The English Football League Championship (often referred to as the Championship for short or the Sky Bet Championship for sponsorship reasons) is the highest division of the English Football League and second-highest overall in the English football league system, after the Premier League.  Each year, the top finishing teams in the Championship are promoted to the Premier League, and the lowest finishing teams are relegated to League One.

Dastur: A dastūr, sometimes spelt dustoor, is a term for a Zoroastrian high priest who has authority in religious matters and ranks higher than a mobad or herbad.  In this specific sense, the term is used mostly among the Parsis of India.

Question: What league ranks higher than the one that Lewis Wing plays in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "football_player_name": {
      "type": "string",
      "description": "The name of the football player."
    },
    "player_club": {
      "type": "string",
      "description": "The club the player plays for."
    },
    "player_league": {
      "type": "string",
      "description": "The league the player's club is in."
    },
    "player_league_rank_description": {
      "type": "string",
      "description": "Description of the player's league rank within its system."
    },
    "higher_ranked_league": {
      "type": "string",
      "description": "The name of the league that ranks higher than the player's league."
    }
  },
  "required": [
    "football_player_name",
    "player_club",
    "player_league",
    "player_league_rank_description",
    "higher_ranked_league"
  ],
  "additionalProperties": false
}
