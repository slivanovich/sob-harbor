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
Toronto Alliance for the Performing Arts: Toronto Alliance for the Performing Arts (TAPA) is an arts service organization representing professional theatre, dance and opera companies in the City of Toronto.  Amongst their 175 members are the Canadian Opera Company, Luminato, Factory Theatre, Mirvish Productions, and Theatre Passe Muraille.  As a lobby and advocacy group, it has been credited with playing a major role in raising Toronto's theatrical profile.  TAPA also presents the annual Dora Mavor Moore Awards, operates T.O. TIX (Toronto's central ticketing outlet), and publishes "Go Live Toronto", an online guide to theatre, dance and opera performances in the city.  In 2008, the organization published a detailed survey of Toronto's performing arts groups, the first of its kind to be conducted there.

Brno City Theatre: Brno City Theatre (Czech: Městské divadlo Brno, further in text MdB) is a repertoire theatre in Brno, Czech Republic, that focuses on dramatic and music production, mainly musical theatre.  The building of the theatre is located on Lidická street in town square Brno-center.  It has two acting areas – dramatical scene (capacity 365 places) and musical theatre scene (capacity 680 places).  As of 2011, the manager and director of the theatre is Stanislav Moša, art manager of the musical ensemble is Petr Gazdík and operetta manager is Igor Ondříček.

Ed Mirvish Theatre: The Ed Mirvish Theatre is a historic film and play theatre in Downtown Toronto, Ontario, Canada.  It was initially known as the Pantages Theatre, then became the Imperial Theatre and later the Canon Theatre, before it was renamed in honour of Ed Mirvish, a well-known businessman and theatre impresario.  The theatre was first opened in 1920 and is located near Yonge-Dundas Square.

David Mirvish: David Mirvish, {'1': ", '2': ", '3': ", '4': "} (born August 29, 1944) is a Canadian art collector, art dealer, theatre producer, real estate developer and son of the late Toronto discount department store owner "Honest" Ed Mirvish and artist Anne Lazar Macklin.

David Mirvish Gallery: David Mirvish Gallery was a contemporary, commercial art gallery run by David Mirvish from 1963 to 1978, within the Markham Street art community on Mirvish Village in Toronto, Ontario, Canada.  Artists at the gallery are best known for Color Field and Post-painterly Abstraction works.  Mirvish assembled the Mirvish Collection, consisting of mostly contemporary artwork including artists he represented, lending it out to museums around the United States and Europe after the gallery's closure.  In 2012, Mirvish announced plans to open a gallery to display these works, at planned condominium project Mirvish+Gehry Toronto.

Mirvish+Gehry: Mirvish+Gehry is an approved building complex in Toronto, Ontario, Canada.  It was designed by Frank Gehry in partnership with David Mirvish.

Osvobozené divadlo: Osvobozené divadlo (1926–1938) ("Liberated Theatre" or "Prague Free Theatre") was a Prague avant-garde theatre scene founded as the theatre section of an association of Czech avant-garde artists Devětsil ("Butterbur") in 1926.  The theatre's beginnings were strongly influenced by Dadaism and Futurism, later by Poetism (a specific Czech art movement).  The theatre was also very leftist oriented, however, it was critical also towards communists.  One of the founders, Jiří Frejka, came up with the name in 1926.  In the theatre both authorial plays and works by well-established modern authors; such as G. Apollinaire, A. Jarry, J. Cocteau, A. Breton, F. T. Marinetti, and V. Nezval were performed.  The modern conception of the scene also laid more emphasis on lighting and the theatrical conception adjured more cooperation and contacts between actors and audience.

G. Sankara Pillai: G. Sankara Pillai (22 June 1930 - 1 January 1989) was an Indian playwright, critic, and director who explored total theatre in a wide range of forms.  He was one of the most versatile and towering personalities of Indian literature and the theatre scene.  His symbolist works were instrumental in defining modern Malayalam theatre.  The Nataka Kalari movement started by Sankara Pillai in 1967 has created some of the best theatre practitioners in the country.  He won the Kerala Sahitya Akademi Award in 1964 for the work "Rail Palangal".  He also won the Sangeet Natak Akademi Award for Theatre-Playwriting in 1979.

Vittorio Rossi: Vittorio Luciano Rossi (born April 16, 1961) is a playwright, actor and screenwriter born in Montreal, Canada.  He grew up in the district of Ville Emard.  Graduating from Concordia University in 1985 with a B.F.A. specializing in theatre performance, Rossi has earned the respect of the national theatre community with his award-winning plays.  Mr. Rossi stormed the Montréal theatre scene with two consecutive Best New Play Awards at the Quebec Drama Festival in 1986 and 1987.  His plays have been produced in Montreal, Toronto, Ottawa, Vancouver, New York City, Boston, Syracuse and The Stratford Festival in Ontario.  Vittorio Rossi is widely considered to be the inaugural Italian-Canadian voice on the English-Canadian stage.

Ed Mirvish: Edwin "Honest Ed" Mirvish, (July 24, 1914 – July 11, 2007) was an American-Canadian businessman, philanthropist and theatrical impresario who lived in Toronto, Ontario.  He is known for his flagship business, Honest Ed's, a landmark discount store in downtown Toronto, and as a patron of the arts, instrumental in revitalizing the theatre scene in Toronto.

Question: Which parent of David Mirvish was instrumental in revitalizing the theatre scene in Toronto?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person identified."
    },
    "relationship_to_david_mirvish": {
      "type": "string",
      "description": "The relationship of the identified person to David Mirvish."
    },
    "role_in_theatre_revitalization": {
      "type": "string",
      "description": "Description of their role in revitalizing the theatre scene."
    },
    "location_of_impact": {
      "type": "string",
      "description": "The city where the theatre scene was revitalized."
    }
  },
  "required": [
    "person_name",
    "relationship_to_david_mirvish",
    "role_in_theatre_revitalization",
    "location_of_impact"
  ],
  "additionalProperties": false
}
