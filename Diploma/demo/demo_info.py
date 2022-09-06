

from Diploma.data.finance_data import FINANCE_DATA


column_groups = {
    'Flight info': ['Productivity',
                    'Productivity to ideal',
                    'Fuel burnt per flight',
                    'Fuel economy to ideal',
                    'Flight cost',
                    'Ecost for trasnp 1 unit'],
    'Leasing info': ['Cost under loan',
                     'Cost under leasing',
                     'Residual leasing value'],
    'Charges': ['Airport charges',
                'Route service fees',
                'Air navigation charges']
}

STAGES = ["Flight info",
          "Loan or leasing",
          "Airport charges",
          'ALL']
