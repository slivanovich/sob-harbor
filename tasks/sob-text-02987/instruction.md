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
Downtown Concord Historic District: The Downtown Concord Historic District encompasses most of the commercial heart of downtown Concord, New Hampshire, United States.  Incorporated in 1734, Concord became the state capital in 1808 and the seat of Merrimack County in 1823.  Economic growth followed, due in part to these government institutions and also to the rise of industry along the Merrimack River, which flows through the city east of the downtown area, and the arrival in the 1840s of the railroad.  The New Hampshire State House was built in 1819 south of the traditional center of the city (now the Concord Historic District), and the commercial heart of the city began to take shape along the First New Hampshire Turnpike south of the State House (now Main Street).  The district was listed on the National Register of Historic Places in 2000.

Hooksett, New Hampshire: Hooksett is a town in Merrimack County, New Hampshire, United States.  The population was 13,451 at the 2010 census.  The town is located between Manchester, the state's largest city, and Concord, the state capital.  A prominent landmark is Robie's Country Store, a National Historic Landmark and a frequent stop for presidential candidates during the New Hampshire primary.

Dunbarton, New Hampshire: Dunbarton is a town in Merrimack County, New Hampshire, United States.  The population was 2,758 at the 2010 census.

South Sutton, New Hampshire: South Sutton is an unincorporated community in the town of Sutton in Merrimack County, New Hampshire, United States.  It is located along New Hampshire Route 114, which leads north through Sutton Mills and North Sutton into the town of New London, and south into the town of Bradford.  South Sutton is located along the Lane River.

Merrimack County Courthouse: The Merrimack County Courthouse stands at 163 North Main Street in Concord, New Hampshire, the state capital and county seat of Merrimack County.  The oldest part of the courthouse building is a brick and granite two story structure, completed in 1857 to serve as a town hall and court building.  The city and county used the building for town offices and county courts until 1904, when the city sold its interest in the building to the county.  Between 1905 and 1907 the building was extensively remodeled to plans by local architect George S. Forrest.  A modern addition has been made to the rear of the building.

Bradford, New Hampshire: Bradford is a town in Merrimack County, New Hampshire, United States.  The population was 1,650 at the 2010 census.  The main village of the town, where 356 people resided at the 2010 census, is defined as the Bradford census-designated place (CDP), and is located in the northeast part of the town, west of the junction of New Hampshire routes 103 and 114.  The town also includes the villages of Bradford Center and Melvin Mills.

Robert W. Upton: Robert William Upton (February 3, 1884April 28, 1972) was a United States Senator from New Hampshire.  Born in Boston, Massachusetts, he attended the public schools, graduated from Boston University Law School in 1907, was admitted to the Massachusetts and New Hampshire bars in 1907 and commenced practice in Concord, New Hampshire.  He was a member of the New Hampshire House of Representatives in 1911 and was a delegate to the New Hampshire State Constitutional Conventions of 1918, 1930, 1938, and 1948, serving as president in 1948.

Samuel Bell: Samuel Bell (February 9, 1770December 23, 1850) was an American politician and lawyer who served as the 14th Governor of New Hampshire from 1819 to 1823, and as the United States Senator for New Hampshire from 1823 to 1835.  Born in Londonderry in the Province of New Hampshire, Bell became a lawyer in the 1790s, and entered politics by becoming a member of the New Hampshire House of Representatives in 1804.  In 1806, the year he left the House, he became the head of a bank which during his tenure in that position became the only New Hampshire bank to fail between 1792 and 1840.  A member of the New Hampshire Senate from 1807 to 1809, and an associate justice of the New Hampshire Supreme Court from 1816 to 1819, Bell was elected to become the Governor of New Hampshire in 1819 as Democratic-Republican.  Re-elected in 1820, 1821, and 1822 against token opposition, Bell's victory in 1822 was accompanied by the largest share of votes cast for a governor candidate of New Hampshire since John Taylor Gilman's victory in 1795.  Whilst Governor, New Hampshire's crime level fell, and industry within the state prospered.  In 1823, declining to stand again for the governorship, he became a Senator for New Hampshire.  He won re-election in 1829, was the chairman of the United States Senate Committee on Claims, and left the Senate in 1835.  He retired from public life thereafter, and died in Chester, New Hampshire at the age of 80.  He is buried in Chester Village Cemetery, Rockingham, New Hampshire.

Austin F. Pike: Austin Franklin Pike (October 16, 1819October 8, 1886) was a United States Representative and Senator from New Hampshire.  Born in Hebron, New Hampshire, he pursued an academic course, studied law, and was admitted to the bar of Merrimack County in 1845.  He was a member of the New Hampshire House of Representatives from 1850 to 1852 and in 1865–1866, and served as speaker during the last two years.  He was a member of the New Hampshire Senate in 1857–1858, serving as president the last year.

Henry E. Burnham: Henry Eben Burnham (November 8, 1844February 8, 1917) was a United States Senator from New Hampshire.  Born in Dunbarton, New Hampshire, he attended the public schools and Kimball Union Academy and married Ella Knowles Haskell, the first woman to argue a case in the U.S. Supreme Court.  Burnham graduated from Dartmouth College in 1865, studied law, was admitted to the bar in 1868 and commenced practice in Manchester.  He engaged in banking and insurance and was member of the New Hampshire House of Representatives in 1873-1874, was treasurer of Hillsborough County from 1875 to 1877, was judge of probate for Hillsborough County from 1876 to 1879, and was a member of the State constitutional convention of 1889.  He was chairman of the Republican State convention in 1888, served as a ballot-law commissioner from 1892 to 1900, and was elected as a Republican to the U.S. Senate in 1901.

Question: Henry Eben Burnham,  was a United States Senator from New Hampshire, he was born in Dunbarton, a town in Merrimack County, New Hampshire, in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "place_of_birth": {
      "type": "string",
      "description": "The town or city where the person was born."
    },
    "state_of_birth": {
      "type": "string",
      "description": "The state where the person was born."
    },
    "county_of_birth_place": {
      "type": "string",
      "description": "The county where the birth place is located."
    },
    "country_of_birth": {
      "type": "string",
      "description": "The country where the person was born."
    }
  },
  "required": [
    "person_name",
    "place_of_birth",
    "state_of_birth",
    "county_of_birth_place",
    "country_of_birth"
  ],
  "additionalProperties": false
}
