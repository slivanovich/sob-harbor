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
Save Austria: Independent Citizens' Initiative Save Austria (German: "Unabhängige Bürgerinitiative Rettet Österreich" ) or Save Austria (German: "Rettet Österreich" ) is an anti-EU movement in Austria which was founded by former presidential candidate and pro-neutrality activist Karl Walter Nowak to fight against the European Constitution and the Treaty of Lisbon.  In the Austrian legislative election, 2008 they received 0.73% of the vote and no seats.  Their largest vote - 0.9% - was in Upper Austria.

Neutral Free Austria Federation: The Neutral Free Austria Federation (German: "Bündnis Neutrales Freies Österreich" , NFÖ) is a political party in Austria founded on 17 March 2003.  It contested the 2006 legislative election under the name "EU Withdrawal – Neutral Free Austria" ("EU-Austritt – Neutrales Freies Österreich"), but only appeared on the ballot in Vorarlberg, Tyrol, Carinthia, Salzburg and Vienna and failed to pass the electoral threshold of 4%, achieving only 0.23%.  Its party program is oriented on Christian politics and centered mainly on the demand to withdraw from the European Union and the establishment of direct democracy.  <br> For the EU election 2014, together with the EU Exit Party (EU-Austrittspartei) which has very similar aims, the party has formed an electoral platform called "EU-STOP".  <br> For the Viennese election 2015, it formed another electoral alliance with the EU Exit Party.  <br> For the legislative election 2017, party leader Rudolf Pomaroli stands on the list of the FLÖ.

Austrian presidential election, 1951: The Austrian presidential elections of 1951 marked the first time that the President of Austria was elected by popular vote.  A constitutional amendment in 1929 would have seen the President being elected directly, however a planned popular election in 1931 was cancelled and moved to the parliament, since it was deemed too expensive.  After the suspension of the constitution in 1934 and Austria ceasing to exist in 1938, the first presidential elections by popular vote were to be held in 1945.  Because the Allied council did not approve on the constitutional law passed by the National Council, the election was again held by the Federal Council of Austria.  With no candidate achieving a majority of the votes, a second round was held on 27 May 1951.  It saw socialist Theodor Körner, mayor of Vienna, defeating the governor of Upper Austria, Heinrich Gleißner of the Austrian People's Party.

Salvadoran presidential election, 1972: Presidential elections were held in El Salvador on 20 February 1972.  The result was a victory for Arturo Armando Molina of the Party of National Conciliation (PCN), who received 43.4% of the vote.  However, the election was characterised by massive fraud.  The PCN had faced a strong challenge from left- and right-wing opposition, and as a result had tried to rig the election by holding the presidential elections two weeks before the legislative election (which took place on 12 March) to ensure that if Molina failed to pass the 50% mark, the Legislative Assembly would still be under PCN control to approve him as president.  Despite their attempts to stuff ballot boxes, it looked for a while as though José Napoleón Duarte of the opposition National Opposing Union (UNO, a coalition of the Christian Democratic Party National Revolutionary Movement and Nationalist Democratic Union) had been victorious after the Central Election Board in San Salvador issued a statement that Duarte had won by around 6,000 votes.  However, this was followed by a three-day news blackout, after which a revised set of figures was announced giving a narrow victory to Molina, meaning that the Legislative Assembly (with a PCN majority) would choose the president.  The opposition walked out of the vote, resulting in Molina being elected by 31 votes to zero.

Citizens' Forum Austria: The Citizens' Forum Austria (German: "Bürgerforum Österreich" , FRITZ) is an Austrian political party mainly active in Tyrol.  It was founded by president of the Tyrolean branch of the Austrian Chamber of Labour Fritz Dinkhauser (an Austrian People's Party member before that), who was joined by the popular anti-transit activist Fritz Gurgiser of the "Transitforum Austria-Tirol".  At the 2008 state election, the Citizens' Forum stood under the name "Fritz Dinkhauser List – Citizens' Forum Tyrol" (German: "Liste Fritz Dinkhauser − Bürgerforum Tirol" , FRITZ) and got 18.3% of the vote, thus becoming the second-largest party with seven seats.  The party contested the 2008 early national election as well, but received only 1.76% of the vote and failed to obtain a seat.  In the 2013 state election, the Citizens' Forum garnered 5.64% of the vote, winning two seats in the state legislature.

Finnish presidential election, 1931: Two-stage presidential elections were held in Finland in 1931.  On 15 and 16 January the public elected presidential electors to an electoral college.  They in turn elected the President.  The result was a victory for Pehr Evind Svinhufvud, who won on the third ballot by just two votes.  The turnout for the popular vote was 47.3%.  This presidential election was held during an ideologically, politically, socially and economically tense time.  The Great Depression was impoverishing many Finnish farmers and workers.  The far-right Lapua Movement had not settled for the ban of the Communist Party and its affiliated organizations in the autumn of 1930.  It wanted to help elect a President who would also strongly oppose the Social Democrats and moderate bourgeois parties, such as the Progressives.  Although Svinhufvud disapproved of the Lapua Movement's violent kidnappings of left-wing politicians and other illegal acts, he was their preferred presidential candidate.  Former President K.J. Ståhlberg, a champion of democracy, parliamentarism and the rule of law, had been briefly kidnapped by some activists of the Lapua Movement with his wife in October 1930.  He was chosen as the Progressive presidential candidate.  Speaker of the Finnish Parliament, Kyösti Kallio, held ideals similar to those of Ståhlberg, and he became the Agrarian presidential candidate.  The outgoing President, Lauri Kristian Relander, had lost the Agrarian presidential candidacy to Kallio, because he did not condemn the Lapua Movement as strongly as Kallio did, and a sufficient number of Agrarians believed that Kallio could control the Lapua Movement's extremists more effectively than Relander.  Right-wing Finns and some centrists, such as a prominent Agrarian parliamentarian, Juho Niukkanen, were concerned that Ståhlberg's re-election (after a six-year break) as the Finnish President would escalate political tensions in Finland.  The Commander-in-Chief of the Civil Guards (a bourgeois voluntary defence organization), Major General Lauri Malmberg, announced in the Finnish Parliament that he would not guarantee order among the Civil Guards, if Ståhlberg was elected President.  Svinhufvud's razor-thin victory required Niukkanen's arm-twisting tactics, whereby he pressured all the Agrarian presidential electors to support Svinhufvud.  This 69-year-old and slightly ailing conservative politician was considered by his supporters as a sufficiently bold, solid and patriotic man to re-unite the ideologically divided Finns.  His pro-democracy supporters hoped that he could keep both right-wing extremists and left-wing extremists in check (see, for example, Sakari Virkkunen, Finland's Presidents I / Suomen presidentit I. Helsinki: Otava Ltd., 1994, pgs.  242-245 (Relander), pgs.  11-14 (Svinhufvud); Pentti Virrankoski, A History of Finland / Suomen historia, volumes 1&2.  Helsinki: Finnish Literature Society / Suomalaisen kirjallisuuden seura, 2009, pgs.  810-816; Raimo Salokangas, "The Independent Republic" (Itsenäinen tasavalta), pgs.  635-639 in Seppo Zetterberg et al., eds., A Small Giant of the Finnish History / Suomen historian pikkujättiläinen.  Helsinki: WSOY, 2003).

Austrian legislative election, 2008: A legislative snap election for the National Council in Austria was held on 28 September 2008.  The previous election was held on 1 October 2006.  The election (the 24th in Austrian history) was caused by the withdrawal of Austrian People's Party leader Wilhelm Molterer from the governing grand coalition (led by the Social Democratic Party of Austria) on 7 July 2008.  Due to dissatisfaction with the grand coalition and the two main parties, it was widely expected to be a realigning election, with gains for the opposition and up to seven parties expected to be in the National Council after the election.  The losses for the government parties (both the SPÖ and the ÖVP had the worst election result in history) resulted in strong gains for the far right, while neither the Liberal Forum nor the Citizens' Forum Austria (both of which were considered to have chances of gaining seats) gained as much as 2% of the vote, defying earlier expectations.  The result of the election was seen as strong for the far-right and in support of Eurosceptics.

Independent Ecological Movement: The Independent Ecological Movement ("Mouvement Ecologiste Indépendant") is a political party in France founded by Antoine Waechter, former presidential candidate of The Greens in 1994.  The MEI hoped to replace the Greens as the major green party, but due to the Green's electoral deals with larger parties, it failed to do so.  They claim to be purely ecologist, and neither on the left or right.  Waechter failed to win enough endorsements to be a candidate in the French presidential election, 1995.  The party ran candidates in the 2004 regional elections and in the European Parliament election, 2004 (France) and were able to prevent the Greens from gaining more seats, such as in the Eastern EU parliamentary region where the MEI's 3% were enough to prevent the Greens from taking 2 seats there instead of one.

Austrian presidential election, 1998: The Austrian presidential election of 1998 was won by the incumbent president Thomas Klestil, who sought re-election as an independent candidate.  The Austrian People's Party, who had originally put him up in 1992, reluctantly supported him again, while the Austrian Social Democratic Party and the Austrian Freedom Party did not propose any competing candidates.  Klestils competitors were Heide Schmidt, leader of the Liberal Forum, Gertraud Knoll, the former Lutheran superintendent of Burgenland (supported by the Greens), socialite Richard Lugner and Karl Walter Nowak.

Tyrolean state election, 2008: The Tyrolean state election of 2008 was held in the Austrian state of Tyrol on 8 June 2008, brought forward from the original date of 5 October 2008 to "avoid collisions with a possible early parliamentary election".  Apart from the Austrian People's Party, the Social Democratic Party of Austria, The Greens – The Green Alternative and the Freedom Party of Austria, the president of the Tyrolean branch of the Austrian Chamber of Labour Fritz Dinkhauser (up to now an ÖVP member) contested the election with a new party called "Bürgerforum Tirol" (Citizens' Forum Tyrol), although initially considered likely to be called "Für Tirol" (For Tyrol), to break the hold of the conservative, farmer-dominated Tyrolean ÖVP on the state (it had an absolute majority in the "Landtag" since the Second World War); Fritz Gurgiser of the "Transitforum Austria-Tirol" will run on Dinkhauser's list.  The federal ÖVP has clearly stated its refport for the incumbent "Landeshauptmann" Herwig van Staa.  The Alliance for the Future of Austria planned to contest the election in a joint list with another split from the FPÖ (the Free Party for Tyrol, "Freie Partei Tirol", FPT) under the name "Alliance of Free Tyroleans" ("Bündnis Freier Tiroler").  On 24 April 2008, it was reported that this list might fail to gather the necessary signatures to contest the election, as the BZÖ suddenly decided not to run under the list's name.  The chairman of the FPT Willi Tilg stated on 2 May 2008 that the party would not contest the election, despite the fact that he claimed they had gathered the necessary signatures; Tilg called on voters to vote for the incumbent governor van Staa instead.  Thanks to the unexpected refport of the Greens, the Communist Party of Austria will be able to contest the election in all of Tyrol.

Question: Independent Citizens' Initiative Save Austria, or Save Austria,  is an anti-EU movement in Austria which was founded by former presidential candidate and pro-neutrality activist Karl Walter Nowak, in the Austrian legislative election, 2008 they received 0.73% of the vote and no seats, it was held on which date?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "election_name": {
      "type": "string",
      "description": "The name of the legislative election."
    },
    "election_year": {
      "type": "integer",
      "description": "The year the election was held."
    },
    "election_date": {
      "type": "string",
      "description": "The specific date the election was held."
    },
    "country": {
      "type": "string",
      "description": "The country where the election took place."
    },
    "related_movement": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the anti-EU movement mentioned."
        },
        "founder": {
          "type": "string",
          "description": "The founder of the anti-EU movement."
        }
      },
      "required": [
        "name",
        "founder"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "election_name",
    "election_year",
    "election_date",
    "country",
    "related_movement"
  ],
  "additionalProperties": false
}
