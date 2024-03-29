import pandas as pd

abbrev2state = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming',
    'PR': 'Puerto Rico',
    'VI': 'Virgin Islands'
}
abbrev2state = {k.lower(): v for k, v in abbrev2state.items()}


df = pd.read_csv('~/Downloads/vehicles.csv')
df['posting_date'] = pd.to_datetime(df['posting_date'], format='%Y-%m-%dT%H:%M:%S%z', utc=True)

# extract the day, month, and year components
df['posting_day'] = df['posting_date'].dt.day
df['posting_month'] = df['posting_date'].dt.month
df['posting_year'] = df['posting_date'].dt.year

# removing trivial columns
trivialColumns = ['posting_date', 'image_url', 'url', 'id', 'description', 'county', 'title_status', 'region_url']
df.drop(trivialColumns, inplace=True, axis=1)

# removing price outliers due to fake listings
# also removing null prices from scraping errors
df = df[(df['price'] < 1000000) & (df['price'] > 100) & (df['price'].notnull())]

# removing odometer outliers
df = df[df['odometer'] < 1000000]

# adding placeholder values for important hierarchies
df['manufacturer'].fillna('Unknown', inplace=True)
df['model'].fillna('Unknown', inplace=True)
df['year'].fillna('Unknown', inplace=True)
df['size'].fillna('Unknown', inplace=True)
df['type'].fillna('Unknown', inplace=True)
df['state'] = df['state'].replace(to_replace=abbrev2state)
df.to_csv('~/Downloads/vehicles_clean.csv', encoding='utf-8', index=False)
