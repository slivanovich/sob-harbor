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
London Conference (1939): The London Conference (1939), or "St James Palace Conference", was called by the British Government to plan the future governance of Palestine and an end of the Mandate.  It opened on 7 February 1939 in St James's Palace after which the Colonial Secretary, Malcolm MacDonald held a series of separate meetings with an Arab and a Jewish delegation, because the Arab delegation refused to sit in the same room as the Jewish delegation.  When MacDonald first announced the proposed conference he made clear that if no agreement was reached the government would impose a solution.  The process came to an end after five and a half weeks with the British announcing proposals which were later published as the 1939 White Paper

Proclamation Gallery: The Proclamation Gallery is a part of St. James Palace in London, England.  It is used after the death of a reigning monarch.  The Accession Council meets to declare the new monarch from the deceased monarch's line, and once the decision is made and the monarch makes a sacred oath to the council they step into the Proclamation Gallery which overlooks Friary Court to make the announcement of the new monarch.

Accession Council: In the United Kingdom, the Accession Council is a ceremonial body which assembles in St James's Palace upon the death of a monarch (Demise of the Crown), to formally proclaim the accession of his or her successor to the throne.  Under the terms of the Act of Settlement 1701, a new monarch succeeds automatically.  The proclamation confirms by name the identity of the heir who has succeeded.

Dawn Approach: Dawn Approach (foaled 23 April 2010) is an Irish Thoroughbred racehorse.  In a racing career which began in March 2012 the colt has won all seven of his races including the Coventry Stakes at Royal Ascot, the National Stakes at the Curragh and the Dewhurst Stakes at Newmarket.  He ended the 2012 European season as the year's most highly rated two-year-old colt and was regarded as a leading contender for the 2013 classics.  As a three-year-old, Dawn Approach won the classic 2000 Guineas on his first appearance, going on to win the St James Palace Stakes at Royal Ascot.

Westminster St James: Westminster St James (or St James Picadilly) was a civil parish in the metropolitan area of London, England.  The creation of the parish followed the building of the Church of St James, Piccadilly in 1684.  After several failed attempts, the parish was formed in 1685 from part of the ancient parish of St Martin in the Fields in the Liberty of Westminster and county of Middlesex.  It included part of the West End of London, taking in sections of Soho, Mayfair and St James's.  Civil parish administration was in the hands of a select vestry until the parish adopted the Vestries Act 1831.  The vestry was reformed again in 1855 by the Metropolis Management Act.  In 1889 the parish became part of the County of London and the vestry was abolished in 1900, replaced by Westminster City Council.  The parish continued to have nominal existence until 1922.

St James' Church, Forest Gate: St James' Church, Forest Gate was a church in Forest Gate, east London.  Its origins lay in an iron building constructed around 1870 to serve a conventional district.  A parish was formed for it in 1881 from those of Emmanuel Church, All Saints and St John's and its permanent church completed the following year, with an organ moved from St Matthew's Church, Friday Street.  The church was demolished in 1964 and for two years its congregation worshiped in the Durning Hall Community Centre's chapel until the parish was merged with that of St John's.  A new church was built for the St James' congregation at northern end of St James Road in 1968.  The congregation finally moved to St Paul's Church, Stratford in 2014, though the area that had formerly been St James' parish was instead transferred from St John's to St Saviour's the same year.

Mark Masons' Hall, London: Mark Masons' Hall in London is the headquarters of The Grand Lodge of Mark Master Masons of England and Wales, which also controls the Royal Ark Mariner degree.  It is located in 86 St James's Street in the central London district of St James's, opposite St James's Palace.  While Freemasons' Hall is the headquarters of the United Grand Lodge of England and the Supreme Grand Chapter of Royal Arch Masons of England, Mark Masons' Hall is the home of several other important appendant orders of Freemasonry in England and Wales.

St James's Street: St James's Street is the principal street in the district of St James's, central London.  It runs from Piccadilly downhill to St James's Palace and Pall Mall.  The main gatehouse of the Palace is at the southern end of the road, and in the 17th century Clarendon House faced down the street across Piccadilly on the site of most of Albemarle Street.

St James' Church, Sydney: St James' Church, commonly known as St James', King Street, is an Anglican parish church in inner city Sydney, Australia, consecrated in February 1824 and named in honour of St James the Great.  It became a parish church in 1835.  Designed in the style of a Georgian town church by the transported convict architect Francis Greenway during the governorship of Lachlan Macquarie, St James' is part of the historical precinct of Macquarie Street which includes other early colonial era buildings such as the Hyde Park Barracks.  The church remains historically, socially and architecturally significant.  The building is the oldest one extant in Sydney's inner city region.  It is listed on the Register of the National Estate, and has been described as one of the world's 80 greatest man-made treasures.

St James's Palace: St James's Palace is the most senior royal palace in the United Kingdom.  Located in the City of Westminster, although no longer the principal residence of the monarch, it is the ceremonial meeting place of the Accession Council and the London residence of several members of the royal family.

Question: Where is the location of St James Palace in whcih the Accession Council assembles upon the death of a monarch?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "palace_name": {
      "type": "string",
      "description": "The name of the palace where the Accession Council assembles."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the palace is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the palace is located."
        },
        "specific_district": {
          "type": "string",
          "description": "The specific district or administrative area within the city where the palace is located."
        }
      },
      "required": [
        "city",
        "country",
        "specific_district"
      ],
      "additionalProperties": false
    },
    "council_assembly_event": {
      "type": "string",
      "description": "The event upon which the Accession Council assembles at the palace."
    }
  },
  "required": [
    "palace_name",
    "location_details",
    "council_assembly_event"
  ],
  "additionalProperties": false
}
