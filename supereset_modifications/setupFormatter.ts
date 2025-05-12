/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
import {
  createDurationFormatter,
  getNumberFormatter,
  getNumberFormatterRegistry,
  NumberFormats,
  getTimeFormatterRegistry,
  SMART_DATE_ID,
  SMART_DATE_DETAILED_ID,
  SMART_DATE_VERBOSE_ID,
  createSmartDateFormatter,
  createSmartDateVerboseFormatter,
  createSmartDateDetailedFormatter,
  NumberFormatter,
  createD3NumberFormatter,
} from '@superset-ui/core';
import { FormatLocaleDefinition, formatLocale } from 'd3-format';
import { TimeLocaleDefinition } from 'd3-time-format';

// Define a custom locale for Indian numbering system (local, not global)
const indianLocale = formatLocale({
  decimal: '.',
  thousands: ',',
  grouping: [3, 2, 2, 2, 2, 2], // Indian digit grouping style
  currency: ['₹', ''],
});

// Function to create Indian number formatter
function createIndianNumberFormatter(): NumberFormatter {
  const formatter = (value: number): string => {
    const absValue = Math.abs(value);
    let formattedValue;
    if (absValue >= 1e7) {
      // Convert to Crores
      formattedValue = `${(value / 1e7).toLocaleString('en-IN', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
      })} Cr`;
    } else if (absValue >= 1e5) {
      // Convert to Lakhs
      formattedValue = `${(value / 1e5).toLocaleString('en-IN', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
      })} L`;
    } else if (absValue >= 1e3) {
      // Convert to Thousands as K
      formattedValue = `${(value / 1e3).toLocaleString('en-IN', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
      })} K`;
    } else {
      // Use Indian digit grouping with no rounding off
      formattedValue = indianLocale.format(',.2f')(value);
    }
    // Ensure the negative sign is handled correctly
    return value < 0 ? `-${formattedValue}` : formattedValue;
  };

  return new NumberFormatter({
    id: 'INDIAN_FORMAT',
    label: 'Indian Number Format (Lakh, Crore)',
    description:
      'Formats numbers in Indian style, with lakh and crore for large numbers.',
    formatFunc: formatter,
  });
}
function createIndianNumberFormatterOnePlace(): NumberFormatter {
  const formatter = (value: number): string => {
    const absValue = Math.abs(value);
    let formattedValue;
    if (absValue >= 1e7) {
      // Convert to Crores
      formattedValue = `${(value / 1e7).toLocaleString('en-IN', {
        minimumFractionDigits: 1,
        maximumFractionDigits: 1,
      })} Cr`;
    } else if (absValue >= 1e5) {
      // Convert to Lakhs
      formattedValue = `${(value / 1e5).toLocaleString('en-IN', {
        minimumFractionDigits: 1,
        maximumFractionDigits: 1,
      })} L`;
    } else if (absValue >= 1e3) {
      // Convert to Thousands as K
      formattedValue = `${(value / 1e3).toLocaleString('en-IN', {
        minimumFractionDigits: 1,
        maximumFractionDigits: 1,
      })} K`;
    } else {
      // Use Indian digit grouping with no rounding off
      formattedValue = indianLocale.format(',.1f')(value);
    }
    // Ensure the negative sign is handled correctly
    return value < 0 ? `-${formattedValue}` : formattedValue;
  };

  return new NumberFormatter({
    id: 'INDIAN_FORMAT',
    label: 'Indian Number Format (Lakh, Crore)',
    description:
      'Formats numbers in Indian style, with lakh and crore for large numbers.',
    formatFunc: formatter,
  });
}
function createIndianNumberFormatterWithRoundingOff(): NumberFormatter {
  const formatter = (value: number): string => {
    const absValue = Math.abs(value);
    let formattedValue;

    if (absValue >= 1e7) {
      // Convert to Crores and round off
      formattedValue = `${Math.round(value / 1e7).toLocaleString('en-IN')} Cr`;
    } else if (absValue >= 1e5) {
      // Convert to Lakhs and round off
      formattedValue = `${Math.round(value / 1e5).toLocaleString('en-IN')} L`;
    } else if (absValue >= 1e3) {
      // Convert to Thousands as K and round off
      formattedValue = `${Math.round(value / 1e3).toLocaleString('en-IN')} K`;
    } else {
      // Use Indian digit grouping with rounding
      formattedValue = indianLocale.format(',d')(Math.round(value));
    }

    // Ensure the negative sign is handled correctly
    return value < 0 ? `-${formattedValue}` : formattedValue;
  };

  return new NumberFormatter({
    id: 'INDIAN_FORMAT_ROUNDED',
    label: 'Indian Number Format (Lakh, Crore, Rounded)',
    description:
      'Formats numbers in Indian style with rounding, using lakh and crore for large numbers.',
    formatFunc: formatter,
  });
}

export default function setupFormatters(
  d3NumberFormat: Partial<FormatLocaleDefinition>,
  d3TimeFormat: Partial<TimeLocaleDefinition>,
) {
  getNumberFormatterRegistry()
    .setD3Format(d3NumberFormat)
    // Add shims for format strings that are deprecated or common typos.
    // Temporary solution until performing a db migration to fix this.
    .registerValue(',0', getNumberFormatter(',.4~f'))
    .registerValue('null', getNumberFormatter(',.4~f'))
    .registerValue('%', getNumberFormatter('.0%'))
    .registerValue('.', getNumberFormatter('.4~f'))
    .registerValue(',f', getNumberFormatter(',d'))
    .registerValue(',r', getNumberFormatter(',.4f'))
    .registerValue('0f', getNumberFormatter(',d'))
    .registerValue(',#', getNumberFormatter(',.4~f'))
    .registerValue('$,f', getNumberFormatter('$,d'))
    .registerValue('0%', getNumberFormatter('.0%'))
    .registerValue('f', getNumberFormatter(',d'))
    .registerValue(',.', getNumberFormatter(',.4~f'))
    .registerValue('.1%f', getNumberFormatter('.1%'))
    .registerValue('1%', getNumberFormatter('.0%'))
    .registerValue('3%', getNumberFormatter('.0%'))
    .registerValue(',%', getNumberFormatter(',.0%'))
    .registerValue('.r', getNumberFormatter('.4~f'))
    .registerValue('$,.0', getNumberFormatter('$,d'))
    .registerValue('$,.1', getNumberFormatter('$,.1~f'))
    .registerValue(',0s', getNumberFormatter(',.4~f'))
    .registerValue('%%%', getNumberFormatter('.0%'))
    .registerValue(',0f', getNumberFormatter(',d'))
    .registerValue('+,%', getNumberFormatter('+,.0%'))
    .registerValue('$f', getNumberFormatter('$,d'))
    .registerValue('+,', getNumberFormatter(NumberFormats.INTEGER_SIGNED))
    .registerValue(',2f', getNumberFormatter(',.4~f'))
    .registerValue(',g', getNumberFormatter(',.4~f'))
    .registerValue('int', getNumberFormatter(NumberFormats.INTEGER))
    .registerValue('.0%f', getNumberFormatter('.1%'))
    .registerValue('$,0', getNumberFormatter('$,.4f'))
    .registerValue('$,0f', getNumberFormatter('$,.4f'))
    .registerValue('$,.f', getNumberFormatter('$,.4f'))
    .registerValue('DURATION', createDurationFormatter())
    .registerValue(
      'DURATION_SUB',
      createDurationFormatter({ formatSubMilliseconds: true }),
    )
    .registerValue('INDIAN_ADAPTIVE_FORMAT', createIndianNumberFormatter())
    .registerValue(
      'INDIAN_ADAPTIVE_.1f_FORMAT',
      createIndianNumberFormatterOnePlace(),
    )
    .registerValue(
      'INDIAN_ROUND_OFF_FORMAT',
      createIndianNumberFormatterWithRoundingOff(),
    )
    .registerValue(
      'INDIAN_NUMBER_FORMAT',
      createD3NumberFormatter({
        locale: {
          decimal: '.',
          thousands: ',',
          grouping: [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], // Indian grouping style
          currency: ['', ''],
        },
        formatString: ',.2f', // Format string to show two decimal places
      }),
    )
    .registerValue(
      'INDIAN_NUMBER_.1f_FORMAT',
      createD3NumberFormatter({
        locale: {
          decimal: '.',
          thousands: ',',
          grouping: [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], // Indian grouping style
          currency: ['', ''],
        },
        formatString: ',.1f', // Format string to show ones decimal places
      }),
    );

  const timeFormatterRegistry = getTimeFormatterRegistry();

  timeFormatterRegistry
    .setD3Format(d3TimeFormat)
    .registerValue(
      SMART_DATE_ID,
      createSmartDateFormatter(timeFormatterRegistry.d3Format),
    )
    .registerValue(
      SMART_DATE_VERBOSE_ID,
      createSmartDateVerboseFormatter(timeFormatterRegistry.d3Format),
    )
    .registerValue(
      SMART_DATE_DETAILED_ID,
      createSmartDateDetailedFormatter(timeFormatterRegistry.d3Format),
    )
    .setDefaultKey(SMART_DATE_ID);
}
