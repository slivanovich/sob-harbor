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
Nature Materials: Nature Materials, is a peer-reviewed scientific journal published by Nature Publishing Group.  It was launched in September 2002.  Vincent Dusastre is the launching and current chief editor.

Diarmuid Johnson: Diarmuid Johnson (1965 -) is a writer.  He was born in Cardiff (Wales), brought up in Galway (Ireland), and holds BA, MA and PhD degrees in Celtic Studies.  He has published poetry and prose in Irish, Welsh and English.  His literary activity extends to the field of translation, and he has authored or co-authored five works of Welsh literature in translation, two in Irish, one in English, one in French, and one in Romanian.  He has also translated poetry from Romanian into English.  Since 2004, he has published a book a year on average.  These include, most recently, 'Conaire Mór - Seacht nDoras na Cinniúna' (2017), a retelling of the Old Irish epic 'Togail Bruidne Da Derga', being one of a planned series with Leabhar Breac; 'Pen and Plough - 20th Century Poets and Bards of Ceredigion (Carreg Gwalch, 2016); 'Rún na mBradán - Dánta Gaeilge 2005-2015 (Coiscéim, 2016).  From 1989 to 1996, Diarmuid Johnson lectured in Celtic Studies in Britanny, Germany and Ireland.  From 1996 until 2000, he worked as a journalist, scriptwriter and translator in Conamara.  He was editor of "Cuisle", a monthly journal in Irish, between 1999 and 2000, and was editor of the trilingual online literary journal "Transcript" from 2002-2004.  He worked at the Mercator Centre for Minority Languages at The University of Aberystwyth from 2002-2006.  The years 2007-2013 he spent lecturing in Poland and Germany.  In 2014, he was bard in residence with Menter Rhos-y-Gilwen in Pembrokeshire, Wales.  He now works as a freelance writer and musician, contributes to Raidió na Gaeltachta and teaches Irish in Ireland in the summer.  He has two daughters, is married, and divides his time between Ireland, Wales, and Brittany.  He also has close ties with Germany, principally in the Rheinland area, where he has been performing and teaching since 2011.

Philip Ball: Philip Ball (born 1962) is a British science writer.  For over twenty years he has been an editor of the journal "Nature" for which he continues to write regularly.  He now writes a regular column in "Chemistry World".  He has contributed to publications ranging from "New Scientist" to the "New York Times", "The Guardian", the "Financial Times" and "New Statesman".  He is the regular contributor to "Prospect" magazine, and also a columnist for "Chemistry World", "Nature Materials" and BBC Future.  He has broadcast on many occasions on radio and TV, and in June 2004 he presented a three-part serial on nanotechnology, "Small Worlds", on BBC Radio 4.

Business and Professional Ethics Journal: Business and Professional Ethics Journal is a peer-reviewed academic journal that examines ethical issues in business encountered by professionals working in large organizational structures.  It provides an outlet for original work that contributes to the development of alternative theories and practices within business and professional ethics, and that examines why global ethical issues, such as poverty alleviation and sustainability, emerge and persist.  The journal is published by the Philosophy Documentation Center in cooperation with the Institute for Business and Professional Ethics at DePaul University.  Members of the Society for Ethics Across the Curriculum have online access to this journal as a benefit of membership.

Gianluca Iacono: Gianluca Iacono (born 14 March 1970 in Turin) is an Italian voice actor.  He contributes to voicing characters in movies, cartoons, anime, and more content.  Iacono is well known for voicing Vegeta in the Italian version of Dragon Ball Z and Dragon Ball GT and Roy Mustang in Fullmetal Alchemist.  Between 2010 and 2011, he temporarily replaced Claudio Moneta as the voice of Kakashi Hatake in Naruto: Shippuden.

Chemistry World: Chemistry World is a monthly chemistry news magazine published by the Royal Society of Chemistry.  The magazine addresses current events in world of chemistry including research, international business news and government policy as it affects the chemical science community, plus the best product applications.  It features regular columns by Philip Ball, Derek Lowe, Andrea Sella and Mark Peplow .  The magazine is sent to all members of the Royal Society of Chemistry and is included in the cost of membership.  In August 2016, the magazine began offering a "soft" paywall option, where a limited amount of content is made available free to all unregistered readers.

Dragon Ball GT: Final Bout: Dragon Ball GT: Final Bout, known in Japan and Europe as Dragon Ball: Final Bout (ドラゴンボール ファイナルバウト , Doragon Bōru Fainaru Bauto ) , is a fighting game for the PlayStation, based on the anime series "Dragon Ball GT".  It was developed and released by Bandai in Japan, parts of Europe, and North America in 1997.  The game was reissued in Europe in 2002 and in North America in 2004.  The game shares the distinction of being the first "Dragon Ball" game to be rendered in full 3D, and the last "Dragon Ball" game produced for the PlayStation.  There would not be another "Dragon Ball" game for consoles until the release of "" in 2002.

Critical Mass (book): Critical Mass: How One Thing Leads to Another is a non-fiction book by English chemist and physicist Philip Ball, originally published in 2004, discusses the concept of a “physics of society”.  Ball examines past thinkers, such as Thomas Hobbes, Lewis Mumford, Emyr Hughes, and Gottfried Achenwall, who have attempted to apply (or argue against) the use of physics, chemistry, or mathematics in the study of mass social phenomena.  He also discusses how the concept relates to recent research, including his own.  Critical Mass was the winner of the 2005 Aventis Prize for Science Books.

Tess Girard: Tess Girard is a Canadian filmmaker and cinematographer most known for her documentary "A Simple Rhythm" a documentary exploring rhythm from the perspective of mathematics, music, biology, philosophy, and psychology, which included interviews with Charles Spearin (of Broken Social Scene, Do Make Say Think, The Happiness Project), and mathematician Steven Strogatz.  The film played at the 2011 Hot Docs Canadian International Documentary Festival, Vancouver International Film Festival 2010, 2011 Rencontres internationales du documentaire de Montréal and 2011 Buenos Aires International Festival of Independent Cinema.  The outtakes of A Simple Rhythm were edited into the radio documentary "The Heart of the Beat" for CBC's Ideas and included additional material with science writer Philip Ball.

Philip Manley Boyce: Philip Manley Boyce (born 20 September 1949) is an Australian psychiatrist.  He is a Professor of Psychiatry and Head of Discipline of Psychiatry at the University of Sydney, and Head of Perinatal Psychiatry Clinical Research Unit at Westmead Hospital.  He has published more than 170 articles and frequently contributes to psychiatric textbooks.  He currently serves as associate editor of Australian and New Zealand Journal of Psychiatry.  He has a long clinical and research interest in anxiety disorders, mood disorders, psychosomatic disorders and perinatal psychiatry.  He has also taken leadership roles in the profession as President of the RANZCP and the international Marcé society, in the development of clinical practice guidelines and in the development of a competency based training program for the College.

Question: Which journal that Philip Ball contributes to was launched in 2002?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "contributor_name": {
      "type": "string",
      "description": "The name of the person who contributes to the journal."
    },
    "journal_name": {
      "type": "string",
      "description": "The name of the journal."
    },
    "launch_year": {
      "type": "integer",
      "description": "The year the journal was launched."
    },
    "launch_month": {
      "type": "string",
      "description": "The month the journal was launched."
    },
    "is_peer_reviewed": {
      "type": "boolean",
      "description": "Indicates if the journal is peer-reviewed."
    }
  },
  "required": [
    "contributor_name",
    "journal_name",
    "launch_year",
    "launch_month",
    "is_peer_reviewed"
  ],
  "additionalProperties": false
}
