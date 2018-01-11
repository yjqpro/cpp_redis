{
  'targets' : [
    {
      'target_name' : 'cpp_redis',
      'type' : '<(component)',
      'sources' : [
        '<!@(python <(DEPTH)/build/glob_files.py sources *.cpp)',
        '<!@(python <(DEPTH)/build/glob_files.py includes *.hpp)',
      ],
      'dependencies' : [
        '<(DEPTH)/third_party/tacopie/tacopie.gyp:tacopie',
      ],
      'include_dirs': [
        '.',
        'includes',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'includes',
		  '<(DEPTH)/third_party/tacopie/includes',
        ],
      },
    },
  ]
}
