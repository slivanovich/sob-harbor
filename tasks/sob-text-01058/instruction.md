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
Midwest Living: Midwest Living is a magazine published by Meredith, is a regional publication that celebrates the richness of life in the American Midwest.  Founded in 1986, the magazine is dedicated to providing its readers a wealth of region-specific information and inspiration, focusing on travel and events, food and dining, and home and garden, as well as other editorial content categories.

Clear Lake (Iowa): Clear Lake is the name of a natural spring fed body of water located in Cerro Gordo County, Iowa near Clear Lake, Iowa.  It is approximately 3684 acre in size.  It is a popular fishing destination, with walleye, bullhead, yellow bass and channel catfish.  People from Des Moines and Minneapolis–Saint Paul have had homes on the shores of the lake since the 1870s.  The average depth is 10 ft and the maximum depth is 30 ft , in the dredged area of the west end.  The lake has 13.6 mi of shoreline.  As of 2004, the lake has seen major efforts undergone to restore its natural clarity, including filtration systems, dredging, and education of local farmers to reduce toxic pesticides from entering the lake.  Clear Lake has been named the "Best Iowa Lake Town" by "The Des Moines Register" and "A Top Vacation Spot" by "Midwest Living" magazine.

Railroad Model Craftsman: Railroad Model Craftsman is an American magazine specializing in the hobby of model railroading.  The magazine is published monthly by White River Productions, which acquired the title from Carstens Publications in 2014.  Its first issue in March 1933 was called The Model Craftsman because it covered other areas of scale modeling as well.  Founded by Emanuele Stieri, it was second owner Charles A. Penn who helped grow the company and lead the publication towards the hobby of scale models.  In April 1949 it changed its focus to model trains and changed its name to Railroad Model Craftsman reflect this change in editorial content.  While it can claim to be the oldest model railroading magazine in continuous publication in the United States, rival "Model Railroader" counters with the tagline "Model railroading "exclusively" since 1934."  (However, both were predated by "The Model Maker," which dates from 1924, and showcased working models of steam engines, trains, and boats.)

Memphis Railroad &amp; Trolley Museum: The Memphis Railroad & Trolley Museum is located at 545 South Main Street on the ground floor of the Central Station in Memphis, Tennessee, USA.  The museum is dedicated to document the local history of Railroad and the Memphis Trolleys.  The museum provides static exhibits as well as video documentation and railroad model diaoramas.

Whatley Historic District: The Whatley Historic District is a historic district in the community of Whatley, Alabama.  Whatley was founded with the establishment of a railroad depot in 1887, along the then-newly constructed railroad between Mobile and Selma.  It was incorporated as a town in 1901.  The historic district features examples of Craftsman, Queen Anne, and regional vernacular architecture.  Spread over 45 acre with 17 contributing buildings and one object, it is roughly bounded by the Whatley Road from Grove Hill to the railroad tracks.  It is a part of the Clarke County Multiple Property Submission and was placed on the National Register of Historic Places on April 30, 1998.

Model Railroad News: Model Railroad News is an American magazine specializing in the hobby of model railroading.  It is the only monthly magazine dedicated exclusively to announcing news of upcoming model releases and reviewing new products in all popular scales.  It was founded in 1995 by Mike Lindsay and Lamplight Publishing, and temporarily ceased publication in October 2011.  The magazine has been published monthly by White River Productions since they acquired the title in 2012.  The editor is Tony Cook, who also serves on the editorial staff of Railroad Model Craftsman and as editor of HO Collector magazine.

Penco: Penco (Mapudungun: "Peumo water") is a Chilean city and commune in Concepción Province, Bío Bío Region on the Bay of Concepción.  Founded as the city of Concepción del Nuevo Extremo ('beginning of the new extreme') on February 12, 1550 by Pedro de Valdivia, it is the third oldest city in Chili, after capital Santiago founded first in 1541 and La Serena second in 1544.

The Craftsman (magazine): The Craftsman was a magazine founded and edited by the American furniture designer Gustav Stickley.  It published architectural designs that were influential in creating the American Craftsman style.  It was a relatively short-lived publication, launching its first issue in October 1901 and its last in December 1916.  The following year, it was merged with "Art World".

Harold H. Carstens: Harold H. Carstens (June 20, 1925 – June 23, 2009) was president of Carstens Publications, publisher of "Railfan & Railroad" and "Railroad Model Craftsman" magazines.  While attending Fairleigh Dickinson University at night, Carstens joined the staff of "Railroad Model Craftsman" in 1952.  While in the Army, he studied art and journalism at the Philippine Institute for the Armed Forces.  The position of managing editor opened up in 1954, and Carstens later advanced to Editor and Vice President in 1957.  When owner Charles Penn retired in 1962, Hal Carstens became President.  In 1973, Carstens moved the company to a new facility in Newton, New Jersey, where it is located today.

Model Railroader: Model Railroader (MR) is an American magazine about the hobby of model railroading.  Founded in 1934 by Al C. Kalmbach, it is published monthly by Kalmbach Publishing of Waukesha, Wisconsin.  Commonly found on newsstands and in libraries, it promotes itself as the oldest magazine of its type in the United States, although it is the long-standing competitor to "Railroad Model Craftsman," which - originally named "The Model Craftsman" - predates MR by one year.

Question: Which magazine was founded first, Midwest Living or Railroad Model Craftsman?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "first_founded_magazine": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the magazine founded first."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the magazine was founded."
        }
      },
      "required": [
        "name",
        "founding_year"
      ],
      "additionalProperties": false
    },
    "second_magazine": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the other magazine in the comparison."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the other magazine was founded."
        }
      },
      "required": [
        "name",
        "founding_year"
      ],
      "additionalProperties": false
    },
    "comparison_summary": {
      "type": "string",
      "description": "A summary statement of which magazine was founded first."
    }
  },
  "required": [
    "first_founded_magazine",
    "second_magazine",
    "comparison_summary"
  ],
  "additionalProperties": false
}
