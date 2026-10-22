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
Anton Shekhovtsov: Anton Shekhovtsov (born 1978) is a Ukrainian writer, academic and political activist.  He is known for his writings on the European radical right and in particular its alleged connections to Russia.  Having worked for the Institute for Euro-Atlantic Cooperation, he is a supporter of the European Union, NATO and liberal democracy, as well as a noted critic of Vladimir Putin's Russia, particularly the ideology of Neo-Eurasianism and the activities of Aleksander Dugin.  He is the editor of the editor of the "Explorations of the Far Right" book series at "ibidem-Verlag" and sits on the board of the open source "Fascism: Journal of Comparative Fascist Studies."

Die Nigger Die!: Die Nigger Die!  is a 1969 political autobiography by the American political activist H. Rap Brown (now known as Jamil Abdullah al-Amin).  The book was first released in the United States in 1969 (by Dial Press) and then in the United Kingdom in 1970 (by Allison & Busby).  Brown describes his experiences as a young black civil rights activist and how they shaped his opinions of white America.  He expresses his opinions on what he believes black Americans need to do to break free from white oppression.  As a Chairman of the Student Nonviolent Coordinating Committee, and from 1968 a member of the Black Panther Party, he was heavily involved with organizations that espoused a Black Power ideology.

James O'Keefe: James Edward O'Keefe III (born June 28, 1984) is an American conservative political activist.  He produces secretly recorded undercover audio and video encounters with figures and workers in academic, governmental and social service organizations, purporting to show abusive or allegedly illegal behavior by employees and/or representatives of those organizations.  He has been criticized for editing videos to misrepresent the context of conversations and the subjects' responses, creating the implication that people said or did things they did not.

Aaron A. Brooks: Aaron A. Brooks, also known as, Aaron Kinsley-Brooks (born January 24, 1964, San Francisco, California) is an American rock musician, drummer, producer and composer.  He co-founded The Little Death with Moby, Laura Dawn and Daron Murphy.  He is a founding member of the American alternative rock band, The Mars Bonfire.  Aaron also plays or has played drums for the electronic pop band Leisure Cruise; Grammy nominated electro-pop chanteuse Angela McCluskey (of Télépopmusik and Wild Colonials); Grammy award-winning producer/songwriter Mark Hudson; Emmy award-winning actress and singer Jackie Cruz; Grammy award-winning artist Moby; Singer/songwriter and progressive political activist Laura Dawn; Grammy award-winning bassist/songwriter and rock musician Duff McKagen of Guns N' Roses; Circle of Soul; Erin Evermore; Grammy award-winning pianist and songwriter A.J. Croce; Grammy winning singer/songwriter Lana Del Ray; Writer, radio host, progressive political comic and guitarist/singer Jamie Kilstein and his band The Agenda; Model/actress/singer/songwriter Heidi Merrill; And NY based rock singer Carleigh Jade.

Laura Loomer: Laura Elizabeth Loomer is an alt-right American political activist and Internet personality.  During the summer of 2017 she was a reporter for Canada's The Rebel Media, until resigning in September.  Prior to June 2017 she worked for Project Veritas with James O'Keefe.

Floyd Westerman: Floyd Westerman, also known as Kanghi Duta i.e. "Red Crow" in Dakota (August 17, 1936 – December 13, 2007), was a Sioux musician, political activist, and actor.  After establishing a career as a country music singer, later in his life, he became a leading actor depicting Native Americans in American films and television.  He is sometimes credited simply as Floyd Westerman.  He worked as a political activist for Native American causes.

Anthony Small: Anthony Small (also known as Abdul Haq) is a retired professional boxer and islamic political activist who was born 20 June 1981 in Lewisham, London, England.  He held both the British and Commonwealth belts at light middleweight.  His was also referred to as 'Sugar Ray Clay Jones Jr.' (SRCJJ), in homage to Sugar Ray Robinson, Sugar Ray Leonard, Muhammad Ali, and Roy Jones Jr..  Small converted to Sunni Islam at the age of 24.  He is active on his YouTube blog where he advocates for Sharia (islamic political ideology) to be implemented in Britain and is a follower of Anjem Choudary and a member of Al-Muhajiroun/Islam4UK.

New Alliance Party: The New Alliance Party (NAP) was an American political party formed in New York City in 1979.  Its immediate precursor was an umbrella organization known as the Labor Community Alliance for Change, whose member groups included the coalition of Grass Roots Women and the New York City Unemployed and Welfare Council.  All of these groups were associated with controversial psychologist and political activist Fred Newman, whose radical health care collective Centers for Change and Marxist International Workers Party were active in grassroots politics in New York City.  The NAP's first chairperson was then-South Bronx City Councilman Gilberto Gerena-Valentin, a veteran Puerto Rican political activist.  .  The party is notable for getting African American psychologist Lenora Fulani on the ballot in all 50 states during her first Presidential campaign in 1988, making her both the first African-American and woman to do so.

Ed Emery (writer): Ed Emery (born 1946) is an ethnomusicologist, writer, translator and political activist.  In the 1970s, he was involved in political activist group Big Flame, and was one of the early organisers of the UK-based Ford Workers' Group.  In 1976, he founded radical publisher Red Notes.  He has translated key works by Italian playwright Dario Fo and political theorist Antonio Negri.  As a writer, he has regularly contributed to Le Monde diplomatique and co-authored two plays with Richard Fredman, "Les Juifs de Salonique" and "The Night Before Larry Was Stretched".  In 2015, for services rendered in the left political movement, he was elected Honorary Member for life of the SOAS Student Union.

Thomas Dixon (politician): Thomas Alan Dixon (born 1952/53) is an American pastor and political activist.  Born in Chicago, he entered the U.S. Navy and worked several jobs before serving time in prison.  Following his release, he became a prominent political activist and was the Democratic nominee in the 2016 United States Senate election in South Carolina.

Question: Laura Loomer previously worked for Project Vertias with a political activist of what ideology?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "activist_name": {
      "type": "string",
      "description": "The name of the political activist."
    },
    "political_ideology": {
      "type": "string",
      "description": "The political ideology of the activist."
    },
    "organization_name": {
      "type": "string",
      "description": "The name of the organization where they worked together."
    },
    "colleague_name": {
      "type": "string",
      "description": "The name of the colleague who worked with the activist."
    }
  },
  "required": [
    "activist_name",
    "political_ideology",
    "organization_name",
    "colleague_name"
  ],
  "additionalProperties": false
}
