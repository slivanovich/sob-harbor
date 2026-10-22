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
Hill–Physick–Keith House: The Hill–Physick–Keith House, also known as the Hill–Keith–Physick House, the Hill–Physick House, or simply the Physick House, is a historic house museum located at 321 S. 4th Street in the Society Hill neighborhood of Philadelphia, Pennsylvania, USA.  Built 1786, it was the home of Philip Syng Physick (1768-1837), who has been called "the father of American surgery".  The house was declared a National Historic Landmark in 1976.  It is now owned and operated by the Philadelphia Society for the Presevation of Landmarks as a house museum.

The Unsinkable Molly Brown (film): The Unsinkable Molly Brown is a 1964 American musical film directed by Charles Walters and starring Debbie Reynolds.  The screenplay by Helen Deutsch is based on the book of the 1960 musical "The Unsinkable Molly Brown" by Richard Morris.  The song score was composed by Meredith Willson.  The plot is a fictionalized account of the life of Margaret Brown, who survived the 1912 sinking of the  .  Debbie Reynolds was nominated for the Academy Award for Best Actress for her portrayal of Brown.

Andrew Brown Donaldson: Andrew Brown Donaldson was a British artist mainly active in the second half of the nineteenth century.  He was born in 1840, although some sources say 1838, and was the second son of a solicitor named William Leverton Donaldson and his wife, Margaret Tennent.  As their name implies, the Donaldsons were of Scottish descent and they were perhaps best known in the nineteenth century for their prominence in the field of architecture; William Leverton Donaldson's father, James Donaldson (1756-1844), and elder brother, Thomas Leverton Donaldson (1795-1885), were both renowned architects.  Margaret Tennent was the daughter of John Tennent of Glasgow and his wife, Margaret Brown, daughter of Andrew Brown, after whom Andrew Brown Donaldson was evidently named.  Inexplicably, Andrew Brown Donaldson is commonly referred to in the art world as Andrew Benjamin Donaldson.

London Town Publik House: The William Brown House, also known as London Town Publik House or Londontowne Public House, is a former Colonial tavern located in the Historic London Town and Gardens museum complex in Woodland Beach, Anne Arundel County, Maryland.  Completed in 1764, it is one of the best-preserved examples of a colonial-era brick tavern house.  From 1828 to 1965 the structure was used as a county alms house.  It was declared a National Historic Landmark in 1970.

Molly Brown House: The Molly Brown House Museum (also known as House of Lions) is a house located at 1340 Pennsylvania Street in Denver, Colorado, United States that was the home of American philanthropist, socialite, and activist Margaret Brown.  Brown was known as "The Unsinkable Molly Brown" because she survived the sinking of the RMS "Titanic".  The museum now located in her former home presents exhibits interpreting her life and that of Victorian Denver as well as architectural preservation.  The house was listed on the National Register of Historic Places in 1972.

Avoca Lodge: Avoca Lodge, known as The Molly Brown Summer House, is a Registered Historic Place in southwest Denver, Colorado near Bear Creek.  The home served as a summer retreat for philanthropist, socialite, and activist Margaret Brown and her husband James Joseph Brown.  It is open to the public rental and for tours.

John Brown House (Chambersburg, Pennsylvania): John Brown House, also known as the Ritner Boarding House, is a historic home located at Chambersburg in Franklin County, Pennsylvania.  It is a two-story, three-bay wide, hewn-log building covered in clapboard.  Abolitionist John Brown (1800–1859) stayed here from June until mid-October 1859, while receiving supplies and recruits for his raid on Harpers Ferry.  Following the raid, four of Brown's followers returned to the house to be concealed.  It is operated by the Franklin County Historical Society - Kittochtinny, as a historic house museum.

Thomas Brown House (Franklin, Tennessee): Old Town, also known as the Thomas Brown House, is a house in Franklin, Tennessee, United States, at the Old Town Archeological Site that was built by Thomas Brown starting in 1846.  It is a two-story frame structure built on an "I-House" plan, an example of vernacular architecture showing Greek Revival influences.  The Thomas Brown House is among the best two-story vernacular I-house examples in the county (along with the William King House, the Alpheus Truett House, the Claiborne Kinnard House, the Beverly Toon House, and the Stokely Davis House).

Margaret Brown: Margaret "Maggie" Brown (née Tobin) (July 18, 1867 – October 26, 1932) (posthumously known as "The Unsinkable Molly Brown") was an American socialite and philanthropist.  She is best remembered for exhorting the crew in Lifeboat No. 6 to return to the debris field of the 1912 sinking of RMS "Titanic" to look for survivors.  Accounts differ on whether the boat actually returned to look for survivors, and if so, if any survivors were found.  During her lifetime, her friends called her "Maggie", but even by her death, obituaries referred to her as the "Unsinkable Mrs. Brown".  The reference was further reinforced by a 1960 Broadway musical based on her life and its 1964 film adaptation which were both entitled "The Unsinkable Molly Brown".

Brown–Ellis House: Brown–Ellis House, also known as the Amos Brown House and Baker House, is a historic home located at Highland, Ulster County, New York.  The house was originally built about 1800, and expanded and renovated in the Greek Revival style about 1835.  It consists of a 1 1/2-story main block with a wing.  It is of timber frame construction and has gable roofs on both sections.  A full width Colonial Revival style front porch was added about 1910.

Question: The Molly Brown House Museum (also known as House of Lions) is a house that was the home of American philanthropist, socialite, and activist Margaret Brown, best known for her survival of what disaster?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of roles or professions associated with the person."
        }
      },
      "required": [
        "name",
        "roles"
      ],
      "additionalProperties": false
    },
    "house": {
      "type": "object",
      "properties": {
        "primary_name": {
          "type": "string",
          "description": "The primary name of the house."
        },
        "alternate_name": {
          "type": "string",
          "description": "An alternate name for the house, if available."
        }
      },
      "required": [
        "primary_name"
      ],
      "additionalProperties": false
    },
    "disaster_survived": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the disaster the person survived."
        },
        "year": {
          "type": "integer",
          "description": "The year the disaster occurred."
        }
      },
      "required": [
        "name",
        "year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person",
    "house",
    "disaster_survived"
  ],
  "additionalProperties": false
}
