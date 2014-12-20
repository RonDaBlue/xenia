# Copyright 2014 Ben Vanik. All Rights Reserved.
{
  'targets': [
    {
      'target_name': 'alloy-ppc-test',
      'type': 'executable',

      'msvs_settings': {
        'VCLinkerTool': {
          'SubSystem': '1',
        },
      },

      'dependencies': [
        'liballoy',
        'libxenia',
      ],

      'include_dirs': [
        '.',
      ],

      'sources': [
        'alloy-ppc-test.cc',
      ],
    },
  ],
}
