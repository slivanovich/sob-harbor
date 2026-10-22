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
Cathedral of the Most Blessed Sacrament: The Cathedral of the Most Blessed Sacrament is a decorated Gothic Revival style Roman Catholic cathedral church in the United States.  It is the seat of the archbishop of the Roman Catholic Archdiocese of Detroit.  The metropolitan archdiocese for the Roman Catholic Ecclesiastical Province of Detroit includes all dioceses in the state of Michigan; in addition, in 2000 the archdiocese accepted pastoral responsibility for the Roman Catholic Church in the Cayman Islands, which consists of Saint Ignatius Parish on Grand Cayman (the Archdiocese of Kingston maintains a "mission sui iuris" jurisdiction over the Cayman Islands).  The cathedral is located at 9844 Woodward Avenue in Detroit, Michigan, adjacent to Detroit's Boston-Edison Historic District.  The cathedral was listed on the National Register of Historic Places in 1982.

St. Patrick's Church: St. Patrick's Church, Saint Patrick's Church, St. Patrick's Roman Catholic Church or Saint Patrick's Roman Catholic Church, and similar, may refer to:

St. Dominic Catholic Church (Miami, FL): St. Dominic Catholic Church was established on May 20, 1962, and is the only Catholic Church in South Florida named in honor of Saint Dominic of Guzman, a 13th-century Catholic saint and founder of the religious Order of Preachers.  Located in 5909 NW 7th Street in Miami, Florida, St. Dominic Catholic Church forms part of the Roman Catholic Archdiocese of Miami.  It consists of 118 parishes and spans a region as far north as Coral Springs, and as far south as Key West, Florida.

Arnold of Soissons: Arnold (Arnoul) of Soissons or Arnold or Arnulf of Oudenburg (ca 1040–1087) is a saint of the Roman Catholic Church, the patron saint of hop-pickers and Belgian brewers.

Roman Catholic Archdiocese of Detroit: The Roman Catholic Archdiocese of Detroit (Latin: "Archidioecesis Detroitensis" ) is an archdiocese of the Latin Rite of the Catholic Church covering (as of 2005) the Michigan counties of Lapeer, Macomb, Monroe, Oakland, St. Clair, and Wayne.  It is the metropolitan archdiocese for the Roman Catholic Ecclesiastical Province of Detroit, which includes all dioceses in the state of Michigan.  In addition, in 2000 the archdiocese accepted pastoral responsibility for the Roman Catholic Church in the Cayman Islands, which consists of Saint Ignatius Parish on Grand Cayman (the Archdiocese of Kingston maintains a mission "sui iuris" jurisdiction over the Cayman Islands).

Rhoda Wise: Rhoda Wise (22 Feb 1888 – 7 July 1948) was a U.S. stigmatist from Canton, Ohio (originally the Roman Catholic Diocese of Cleveland and now part of the Diocese of Youngstown).  Her biography, "Her Name Means Rose", was published by EWTN.  Rhoda Wise has been associated with many miraculous healings, including the healing of Mother Angelica.  The Roman Catholic Church investigated Wise, but made no official decision concerning her experiences .  The Rhoda Wise Shrine, which includes her house- which once belonged to EWTN, which Mother Angelica founded and ran- is a private association of the faithful (website: http://rhodawise.com), that has been approved by the present incumbent Bishop of the Roman Catholic Diocese of Youngstown, Bishop George V. Murry.  As of September 2016, the Diocese is launching the local investigation into a potential cause for beatification and canonization, and so all her visions and writings and activities will be re-examined thoroughly.  If the diocesan process concludes she lived an exemplary life, the case for the cause will go to the Vatican, and with their approval, she will be given the title "Servant of God".  If the Holy See says she lived an admirable life, she will then also be called "Venerable".  Since she is not a martyr, unless the Pope grants some form of exemption, two miracles would then be needed: one for her beatification (being called "Blessed"), and then one for her canonization (sainthood) that must be verified after her beatification (though it can occur before beatification, as long as it occurred after the first miracle happened).  St. Peter Catholic Church, in Canton, Ohio, will host the Mass opening the diocesan investigation into Rhoda Wise’s cause for beatification and canonization.  Monsignor Robert Siffrin, the Vicar General of the Youngstown Catholic Diocese, will celebrate the Mass on Friday, October 7, 2016, at 7:00 PM.

St. Louis Roman Catholic Church: Saint Louis Roman Catholic Church is a Catholic parish in Buffalo, New York.  It was the first Catholic church built in Buffalo, and holds the title of "Mother Church of the Roman Catholic Diocese of Buffalo".

Church of Saint John the Baptist (Pijnacker): The church of Saint John the Baptist (or as written by the parish H. Joannes de Dooper or as a variant in Dutch Sint Johannes de Doper) is a Roman Catholic church in Pijnacker.  The church is cruciform and built in the neo-Roman style.  It was built in 1892 and at that time was within the Roman Catholic Diocese of Haarlem which was later renamed the Roman Catholic Diocese of Haarlem-Amsterdam.  When diocesan boundaries were redrawn it became part of the Roman Catholic Diocese of Rotterdam.  It is the work of architect, Adrianus Bleijs.  The name of the church has several variations.  The parish website officially shows it as "H. Joannes de Dooper," (with no "h" and with two "o"s) but others list it as Heilige (or Sint) Johannes de Doper (with an "h" and with only one "o.")

Tiegem: Tiegem (also, Tieghem) is a village in the municipality of Anzegem, near Oudenaarde, West-Flanders, Belgium.  Tiegem was birthplace of St. Arnold of Soissons.

St. Eric's Cathedral, Stockholm: Saint Eric's Cathedral is a Roman Catholic cathedral in Stockholm, Sweden.  It is located on Södermalm, the southern part of central Stockholm.  It was built in 1892 and was raised to the status of a cathedral in 1953, when the Roman Catholic Diocese of Stockholm was created (still the only one in Sweden).  The substantial increase in the number of Catholics in Stockholm and Sweden, mostly as a result of immigration after World War II, made the old church insufficient, and an extension, designed by architects Hans Westman and Ylva Lenormand, was inaugurated in 1983, at the 200th anniversary of the re-establishment in 1783 of the Roman Catholic Church in Lutheran Sweden.  The block where the cathedral is located also contains other functions serving the Roman Catholic Church in Sweden.

Question: What is the birthplace village of a saint of the Roman Catholic Church who lived from ca 1040–1087?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "saint_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the Roman Catholic saint."
        },
        "lifespan": {
          "type": "string",
          "description": "The approximate years the saint lived."
        }
      },
      "required": [
        "name",
        "lifespan"
      ],
      "additionalProperties": false
    },
    "birthplace_village": {
      "type": "string",
      "description": "The village where the saint was born."
    },
    "is_roman_catholic_saint": {
      "type": "boolean",
      "description": "Indicates if the person is a saint of the Roman Catholic Church."
    }
  },
  "required": [
    "saint_details",
    "birthplace_village",
    "is_roman_catholic_saint"
  ],
  "additionalProperties": false
}
