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
Elmbank Gardens: The Charing Cross Complex - now styled as Elmbank Gardens (but sometimes popularly referred to as the Charing Cross Tower), is a multi-use commercial complex in the Charing Cross area of Glasgow, Scotland.  Best known for its signature 14-storey tower which overlooks the M8 motorway and stands directly opposite the Mitchell Library, it was designed by Richard Seifert and constructed between 1969 and 1973.  It is one of the tallest and most prominent high rise buildings on the western side of Glasgow city centre.  The surface buildings of the subterranean railway station which serves Charing Cross are also an integral part of the complex.

Queen Eleanor Memorial Cross: The Queen Eleanor Memorial Cross is a replica of the medieval Eleanor cross at Charing (London), erected in the forecourt of Charing Cross railway station in 1864–5.  It was designed by Edward Middleton Barry, also the architect of the station, and includes multiple statues of Eleanor of Castile by Thomas Earp.  It does not occupy the original site of the Charing Cross (destroyed in 1647), which is now occupied by Hubert Le Sueur's equestrian statue of Charles I.

Eleanor cross: The Eleanor crosses were a series of twelve lavishly decorated stone monuments topped with tall crosses, of which three survive nearly intact, in a line down part of the east of England.  King Edward I had the crosses erected between 1291 and 1294 in memory of his wife Eleanor of Castile, marking the nightly resting-places along the route taken when her body was transported to London.  Several artists worked on the crosses, as the "Expense Rolls" of the Crown show, with some of the work being divided between the main figures, sent from London, and the framework, made locally.  "Alexander of Abingdon" and "William of Ireland", both of whom had worked at Westminster Abbey, were apparently the leading sculptors of figures.

Ewell West railway station: Ewell West railway station is one of two competing stations in Ewell (in the Epsom and Ewell district) in Surrey.  The station is served by South Western Railway.  It is 12.3 mi from Charing Cross Station in Central London.

As I was going by Charing Cross: "As I was going by Charing Cross" (sometimes referred to as "As I was going to Charing Cross"), is an English language nursery rhyme.  The rhyme was first recorded in the 1840s, but it may have older origins in street cries and verse of the seventeenth century.  It refers to the equestrian statue of King Charles I in Charing Cross, London, and may allude to his death or be a puritan satire on royalist reactions to his execution.  It was not recorded in its modern form until the mid-nineteenth century.  It has a Roud Folk Song Index number of 20564.

Charing Cross tube station: Charing Cross (sometimes informally abbreviated as Charing X) is a London Underground station at Charing Cross in the City of Westminster with entrances located in Trafalgar Square and The Strand.  The station is served by the Northern and Bakerloo lines and provides an interchange with the National Rail network at Charing Cross station.  On the Northern line it is between Embankment and Leicester Square stations on the Charing Cross branch, and on the Bakerloo line it is between Embankment and Piccadilly Circus stations.  The station is in Travelcard Zone 1.  The station was served by the Jubilee line between 1979 and 1999, acting as the southern terminus of the line during that period.

Charing Cross Theatre: Previously called the New Players' Theatre and founded in 1936, the Charing Cross Theatre occupied several premises in the West End of London before locating to its present site under The Arches off Villiers Street below Charing Cross station.  The current site was a famous Victorian music hall The Players' Theatre.  It was refurbished in 2005 and taken under new management in 2006 and reopened as 'The New Players Theatre'.

Charing Cross Road: Charing Cross Road is a street in central London running immediately north of St Martin-in-the-Fields to St Giles Circus (the intersection with Oxford Street) and then becomes Tottenham Court Road.  It is so called because it serves Charing Cross railway station (named for the nearby Charing Cross).

Charing Cross (Glasgow) railway station: Charing Cross (Glasgow) is a railway station close to the centre of Glasgow, Scotland, serving the district of the same name.  It is managed by Abellio ScotRail and is served by trains on the North Clyde Line.  It should not be confused with the Charing Cross station in London.

Imperial Camel Corps Memorial: The Imperial Camel Corps Memorial is an outdoor sculpture commemorating the Imperial Camel Corps, located in Victoria Embankment Gardens, on the Thames Embankment to the east of Charing Cross station, in London, England.  The unit of mounted infantry was created in December 1916 from troop that had served in the Gallipoli campaign in the Dardanelles.

Question: Which king had erected the original memorials of which the The Queen Eleanor Memorial Cross at Charing Cross Station is a replica  ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "king_who_erected_memorials": {
      "type": "string",
      "description": "The name of the king who had the original memorials erected."
    },
    "original_memorial_type": {
      "type": "string",
      "description": "The type of the original memorials."
    },
    "person_commemorated": {
      "type": "string",
      "description": "The name of the person in whose memory the original memorials were erected."
    },
    "erection_years": {
      "type": "string",
      "description": "The period during which the original memorials were erected."
    },
    "replica_memorial_name": {
      "type": "string",
      "description": "The name of the replica memorial mentioned in the question."
    }
  },
  "required": [
    "king_who_erected_memorials",
    "original_memorial_type",
    "person_commemorated",
    "erection_years",
    "replica_memorial_name"
  ],
  "additionalProperties": false
}
