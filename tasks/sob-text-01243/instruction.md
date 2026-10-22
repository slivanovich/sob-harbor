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
Ellis County, Kansas: Ellis County (county code EL) is a county located in the U.S. state of Kansas.  As of the 2010 census, the county population was 28,452.  Its county seat and most populous city is Hays.

Falmouth, Indiana: Falmouth is an unincorporated community in Fayette and Rush counties in the U.S. state of Indiana.  Located at the northeastern corner of Union Township and the southeastern corner of Washington Township in Rush County and along the northwestern edge of Fairview Township in Fayette County, it lies at the intersection of CR800E (Rush County) with CR600N (Rush County)/CR400N(Fayette County).  Falmouth sits northwest of Connersville and northeast of Rushville, the county seats of Fayette and Rush counties respectively.  Its elevation is 1,070 feet (326 m), and it is located at (39.7008798, -85.3010781).  Although Falmouth is unincorporated, it has a post office (located in Rush County), with the ZIP code of 46127.

Freedom, Indiana: Freedom is an unincorporated community in western Franklin Township, Owen County, in the U.S. state of Indiana.  It lies along U.S. Route 231, southwest of the city of Spencer, the county seat of Owen County.  Its elevation is 538 feet (164 m), and it is located at (39.2069886, -86.8691740).  Although Freedom is unincorporated, it has a post office, with the ZIP code of 47431.

Catharine, Kansas: Catharine is an unincorporated community and census-designated place (CDP) in Catherine Township, Ellis County, Kansas, United States.  As of the 2010 census, the population of the community was 104.

Crestview Local School District (Richland County): Crestview Local School District is a public school district serving students in the northeastern part of Richland County just north of the city of Mansfield and the northwestern part of Ashland County just northwest of the city of Ashland in the U.S. state of Ohio.  Municipalities and townships that are included in the school district in Richland County are northern parts of the city of Mansfield, most of Franklin Township, all of Weller Township (including the unincorporated community of Olivesburg), all of Butler Township, and southern parts of Blooming Grove Township.  Municipalities and townships that are included in the school district in Ashland County are the villages of Savannah and Bailey Lakes, most of Clear Creek Township, and northwestern parts of Orange Township.  The school district enrolls 1,256 students as of the 2007-2008 academic year.

Freedom Township, Michigan: Freedom Township is a civil township of Washtenaw County in the U.S. state of Michigan.  The population was 1,428 at the 2010 census.  The unincorporated hamlet of Fredonia is located on Pleasant Lake within the township.

Pfeifer, Kansas: Pfeifer is an unincorporated community in Freedom Township, Ellis County, Kansas, United States.

Munjor, Kansas: Munjor is an unincorporated community and census-designated place (CDP) in Wheatland Township, Ellis County, Kansas, United States.  As of the 2010 census, the population of the community was 213.

Drakesburg, Ohio: Drakesburg is an unincorporated community in Portage County, in the U.S. state of Ohio.  It is located in Freedom Township at the intersection of Nichols Road and state routes 303 and 88.

Leelanau County, Michigan: Leelanau County ( ) is a county located in the U.S. state of Michigan.  As of the 2010 census, the population was 21,708.  The county seat was until recently the unincorporated community of Leland.  On August 3, 2004, county voters approved a proposal to move the county seat to Suttons Bay Township, closer to the county's geographic center.  In 2008, the county offices completed their move to a new government center built on 45 acres (180,000 m²) of county-owned land, one mile east of the unincorporated village of Lake Leelanau, where a new county law enforcement center was completed.

Question: Pfeifer is an unincorporated community in Freedom Township, Ellis County, a county located in the U.S. state of Kansas, in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "community_name": {
      "type": "string",
      "description": "The name of the community."
    },
    "is_unincorporated": {
      "type": "boolean",
      "description": "Indicates if the community is unincorporated."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "township": {
          "type": "string",
          "description": "The township where the community is located."
        },
        "county": {
          "type": "string",
          "description": "The county where the community is located."
        },
        "state": {
          "type": "string",
          "description": "The U.S. state where the community is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the community is located."
        }
      },
      "required": [
        "township",
        "county",
        "state",
        "country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "community_name",
    "is_unincorporated",
    "location_details"
  ],
  "additionalProperties": false
}
