{'targets': [{
  'target_name': 'rocksdb',
  'variables': {
    'rdbversion': '4.4'
  },
  'type': 'static_library',
  # Overcomes an issue with the linker and thin .a files on SmartOS
  'standalone_static_library': 1,
  'dependencies': [
    '../snappy/snappy.gyp:snappy'
  ],
  'direct_dependent_settings': {
    'include_dirs': [
      'rocksdb-<(rdbversion)/include/',
      'rocksdb-<(rdbversion)/port/',
      'rocksdb-<(rdbversion)/util/',
      'rocksdb-<(rdbversion)/'
    ]
  },
  'defines': [
    'SNAPPY=1'
    # 'ROCKSDB_LITE=1'
  ],
  'include_dirs': [
    'rocksdb-<(rdbversion)/',
    'rocksdb-<(rdbversion)/include/'
  ],
  # ./rocksdb-4.4/build_tools/build_detect_platform
  'conditions': [
    ['OS == "win"', {
      'conditions': [
        ['MSVS_VERSION != "2015" and MSVS_VERSION != "2013"', {
          'include_dirs': ['rocksdb-<(rdbversion)/port/win']
        }]
      ],
      'include_dirs': [
        'port-libuv/'
      ],
      'defines': [
        'ROCKSDB_PLATFORM_UV=1',
        'NOMINMAX=1',
        '_HAS_EXCEPTIONS=0'
      ],
      'sources': [
        'port-libuv/port_uv.cc',
        'port-libuv/env_win.cc',
        'port-libuv/win_logger.cc'
      ],
      'msvs_settings': {
        'VCCLCompilerTool': {
          'RuntimeTypeInfo': 'false',
          'EnableFunctionLevelLinking': 'true',
          'ExceptionHandling': '2',
          'DisableSpecificWarnings': ['4355', '4530' ,'4267', '4244']
        }
      }
    }, { # OS != "win"
      'sources': [
        'rocksdb-<(rdbversion)/port/port_posix.cc',
        'rocksdb-<(rdbversion)/util/env_posix.cc',
        'rocksdb-<(rdbversion)/util/io_posix.cc',
        'rocksdb-<(rdbversion)/util/thread_posix.cc'
      ],
      'defines': [
        'ROCKSDB_PLATFORM_POSIX=1',
        'ROCKSDB_LIB_IO_POSIX=1'
      ],

      # 'ccflags': [
      #   '-fno-builtin-memcmp',
      #   '-fPIC'
      # ]
      # 'cflags': [ '-std=c++0x' ],
      # 'cflags!': [ '-fno-tree-vrp' ],

      'cflags': [
        '-std=gnu++0x',

        '-fno-builtin-memcmp',

        '-fno-omit-frame-pointer',
        '-momit-leaf-frame-pointer',
        '-Woverloaded-virtual',
        '-Wno-ignored-qualifiers',
        '-Wno-type-limits',
        '-Wno-unused-variable',
        '-Wno-format-security',
        '-fPIC'
      ],
      'cflags!': [
        '-fno-exceptions',
        '-fno-rtti',

        '-fno-tree-vrp'
      ],
      'cflags_cc!': [
        '-fno-exceptions',
        '-fno-rtti'
      ]
    }],
    ['OS != "win"' and 'OS != "freebsd"', {
      'cflags': [
        '-Wno-sign-compare',
        '-Wno-unused-but-set-variable'
      ]
    }],
    ['OS == "linux"', {
      'defines': [
        'OS_LINUX=1'
      ],
      'libraries': [
        '-lpthread',
        '-lrt'
      ],
      'ccflags': [
        '-pthread'
      ]
    }],
    ['OS == "freebsd"', {
      'defines': [
        'OS_FREEBSD=1',
        '_REENTRANT=1'
      ],
      'libraries': [
        '-lpthread'
      ],
      'ccflags': [
        '-pthread'
      ],
      'cflags': [
        '-Wno-sign-compare'
      ]
    }],
    ['OS == "solaris"', {
      'defines': [
        'OS_SOLARIS=1',
        '_REENTRANT=1'
      ],
      'libraries': [
        '-lrt',
        '-lpthread'
      ],
      'ccflags': [
        '-pthread'
      ]
    }],
    ['OS == "mac"', {
      'defines': [
        'OS_MACOSX=1'
      ],
      'libraries': [],
      'ldflags': [
        # '-dynamiclib',
        # '-install_name'
      ],
      'ccflags': [],
      'xcode_settings': {
        'WARNING_CFLAGS': [
          '-Wno-sign-compare',
          '-Wno-unused-variable',
          '-Wno-unused-function'
        ]
      }
    }]
  ],
  # ./rocksdb-4.4/Makefile
  # ./rocksdb-4.4/src.mk
  'sources': [
    'rocksdb-<(rdbversion)/db/builder.cc',
    'rocksdb-<(rdbversion)/db/c.cc',
    'rocksdb-<(rdbversion)/db/column_family.cc',
    'rocksdb-<(rdbversion)/db/compacted_db_impl.cc',
    'rocksdb-<(rdbversion)/db/compaction.cc',
    'rocksdb-<(rdbversion)/db/compaction_iterator.cc',
    'rocksdb-<(rdbversion)/db/compaction_job.cc',
    'rocksdb-<(rdbversion)/db/compaction_picker.cc',
    'rocksdb-<(rdbversion)/db/convenience.cc',
    'rocksdb-<(rdbversion)/db/db_filesnapshot.cc',
    'rocksdb-<(rdbversion)/db/dbformat.cc',
    'rocksdb-<(rdbversion)/db/db_impl.cc',
    'rocksdb-<(rdbversion)/db/db_impl_debug.cc',
    'rocksdb-<(rdbversion)/db/db_impl_readonly.cc',
    'rocksdb-<(rdbversion)/db/db_impl_experimental.cc',
    'rocksdb-<(rdbversion)/db/db_iter.cc',
    'rocksdb-<(rdbversion)/db/experimental.cc',
    'rocksdb-<(rdbversion)/db/event_helpers.cc',
    'rocksdb-<(rdbversion)/db/file_indexer.cc',
    'rocksdb-<(rdbversion)/db/filename.cc',
    'rocksdb-<(rdbversion)/db/flush_job.cc',
    'rocksdb-<(rdbversion)/db/flush_scheduler.cc',
    'rocksdb-<(rdbversion)/db/forward_iterator.cc',
    'rocksdb-<(rdbversion)/db/internal_stats.cc',
    'rocksdb-<(rdbversion)/db/log_reader.cc',
    'rocksdb-<(rdbversion)/db/log_writer.cc',
    'rocksdb-<(rdbversion)/db/managed_iterator.cc',
    'rocksdb-<(rdbversion)/db/memtable_allocator.cc',
    'rocksdb-<(rdbversion)/db/memtable.cc',
    'rocksdb-<(rdbversion)/db/memtable_list.cc',
    'rocksdb-<(rdbversion)/db/merge_helper.cc',
    'rocksdb-<(rdbversion)/db/merge_operator.cc',
    'rocksdb-<(rdbversion)/db/repair.cc',
    'rocksdb-<(rdbversion)/db/slice.cc',
    'rocksdb-<(rdbversion)/db/snapshot_impl.cc',
    'rocksdb-<(rdbversion)/db/table_cache.cc',
    'rocksdb-<(rdbversion)/db/table_properties_collector.cc',
    'rocksdb-<(rdbversion)/db/transaction_log_impl.cc',
    'rocksdb-<(rdbversion)/db/version_builder.cc',
    'rocksdb-<(rdbversion)/db/version_edit.cc',
    'rocksdb-<(rdbversion)/db/version_set.cc',
    'rocksdb-<(rdbversion)/db/wal_manager.cc',
    'rocksdb-<(rdbversion)/db/write_batch.cc',
    'rocksdb-<(rdbversion)/db/write_batch_base.cc',
    'rocksdb-<(rdbversion)/db/write_controller.cc',
    'rocksdb-<(rdbversion)/db/write_thread.cc',
    'rocksdb-<(rdbversion)/memtable/hash_cuckoo_rep.cc',
    'rocksdb-<(rdbversion)/memtable/hash_linklist_rep.cc',
    'rocksdb-<(rdbversion)/memtable/hash_skiplist_rep.cc',
    'rocksdb-<(rdbversion)/port/stack_trace.cc',
    # 'rocksdb-<(rdbversion)/port/port_posix.cc',
    'rocksdb-<(rdbversion)/table/adaptive_table_factory.cc',
    'rocksdb-<(rdbversion)/table/block_based_filter_block.cc',
    'rocksdb-<(rdbversion)/table/block_based_table_builder.cc',
    'rocksdb-<(rdbversion)/table/block_based_table_factory.cc',
    'rocksdb-<(rdbversion)/table/block_based_table_reader.cc',
    'rocksdb-<(rdbversion)/table/block_builder.cc',
    'rocksdb-<(rdbversion)/table/block.cc',
    'rocksdb-<(rdbversion)/table/block_hash_index.cc',
    'rocksdb-<(rdbversion)/table/block_prefix_index.cc',
    'rocksdb-<(rdbversion)/table/bloom_block.cc',
    'rocksdb-<(rdbversion)/table/cuckoo_table_builder.cc',
    'rocksdb-<(rdbversion)/table/cuckoo_table_factory.cc',
    'rocksdb-<(rdbversion)/table/cuckoo_table_reader.cc',
    'rocksdb-<(rdbversion)/table/flush_block_policy.cc',
    'rocksdb-<(rdbversion)/table/format.cc',
    'rocksdb-<(rdbversion)/table/full_filter_block.cc',
    'rocksdb-<(rdbversion)/table/get_context.cc',
    'rocksdb-<(rdbversion)/table/iterator.cc',
    'rocksdb-<(rdbversion)/table/merger.cc',
    'rocksdb-<(rdbversion)/table/meta_blocks.cc',
    'rocksdb-<(rdbversion)/table/sst_file_writer.cc',
    'rocksdb-<(rdbversion)/table/plain_table_builder.cc',
    'rocksdb-<(rdbversion)/table/plain_table_factory.cc',
    'rocksdb-<(rdbversion)/table/plain_table_index.cc',
    'rocksdb-<(rdbversion)/table/plain_table_key_coding.cc',
    'rocksdb-<(rdbversion)/table/plain_table_reader.cc',
    'rocksdb-<(rdbversion)/table/table_properties.cc',
    'rocksdb-<(rdbversion)/table/two_level_iterator.cc',
    'rocksdb-<(rdbversion)/tools/dump/db_dump_tool.cc',
    'rocksdb-<(rdbversion)/util/arena.cc',
    'rocksdb-<(rdbversion)/util/auto_roll_logger.cc',
    'rocksdb-<(rdbversion)/util/bloom.cc',
    'rocksdb-<(rdbversion)/util/build_version.cc',
    'rocksdb-<(rdbversion)/util/cache.cc',
    'rocksdb-<(rdbversion)/util/coding.cc',
    'rocksdb-<(rdbversion)/util/comparator.cc',
    'rocksdb-<(rdbversion)/util/compaction_job_stats_impl.cc',
    'rocksdb-<(rdbversion)/util/concurrent_arena.cc',
    'rocksdb-<(rdbversion)/util/crc32c.cc',
    'rocksdb-<(rdbversion)/util/db_info_dumper.cc',
    'rocksdb-<(rdbversion)/util/delete_scheduler_impl.cc',
    'rocksdb-<(rdbversion)/util/dynamic_bloom.cc',
    'rocksdb-<(rdbversion)/util/env.cc',
    # 'rocksdb-<(rdbversion)/util/env_hdfs.cc',
    # 'rocksdb-<(rdbversion)/util/env_posix.cc',
    # 'rocksdb-<(rdbversion)/util/io_posix.cc',
    # 'rocksdb-<(rdbversion)/util/thread_posix.cc',
    'rocksdb-<(rdbversion)/util/file_util.cc',
    'rocksdb-<(rdbversion)/util/file_reader_writer.cc',
    'rocksdb-<(rdbversion)/util/filter_policy.cc',
    'rocksdb-<(rdbversion)/util/hash.cc',
    'rocksdb-<(rdbversion)/util/histogram.cc',
    'rocksdb-<(rdbversion)/util/instrumented_mutex.cc',
    'rocksdb-<(rdbversion)/util/iostats_context.cc',
    'rocksdb-<(rdbversion)/utilities/backupable/backupable_db.cc',
    'rocksdb-<(rdbversion)/utilities/convenience/info_log_finder.cc',
    'rocksdb-<(rdbversion)/utilities/checkpoint/checkpoint.cc',
    'rocksdb-<(rdbversion)/utilities/compaction_filters/remove_emptyvalue_compactionfilter.cc',
    'rocksdb-<(rdbversion)/utilities/document/document_db.cc',
    'rocksdb-<(rdbversion)/utilities/document/json_document_builder.cc',
    'rocksdb-<(rdbversion)/utilities/document/json_document.cc',
    'rocksdb-<(rdbversion)/utilities/env_mirror.cc',
    'rocksdb-<(rdbversion)/utilities/flashcache/flashcache.cc',
    'rocksdb-<(rdbversion)/utilities/geodb/geodb_impl.cc',
    'rocksdb-<(rdbversion)/utilities/leveldb_options/leveldb_options.cc',
    'rocksdb-<(rdbversion)/utilities/memory/memory_util.cc',
    'rocksdb-<(rdbversion)/utilities/merge_operators/put.cc',
    'rocksdb-<(rdbversion)/utilities/merge_operators/string_append/stringappend2.cc',
    'rocksdb-<(rdbversion)/utilities/merge_operators/string_append/stringappend.cc',
    'rocksdb-<(rdbversion)/utilities/merge_operators/uint64add.cc',
    'rocksdb-<(rdbversion)/utilities/options/options_util.cc',
    'rocksdb-<(rdbversion)/utilities/redis/redis_lists.cc',
    'rocksdb-<(rdbversion)/utilities/spatialdb/spatial_db.cc',
    'rocksdb-<(rdbversion)/utilities/table_properties_collectors/compact_on_deletion_collector.cc',
    'rocksdb-<(rdbversion)/utilities/transactions/optimistic_transaction_impl.cc',
    'rocksdb-<(rdbversion)/utilities/transactions/optimistic_transaction_db_impl.cc',
    'rocksdb-<(rdbversion)/utilities/transactions/transaction_base.cc',
    'rocksdb-<(rdbversion)/utilities/transactions/transaction_db_impl.cc',
    'rocksdb-<(rdbversion)/utilities/transactions/transaction_db_mutex_impl.cc',
    'rocksdb-<(rdbversion)/utilities/transactions/transaction_lock_mgr.cc',
    'rocksdb-<(rdbversion)/utilities/transactions/transaction_impl.cc',
    'rocksdb-<(rdbversion)/utilities/transactions/transaction_util.cc',
    'rocksdb-<(rdbversion)/utilities/ttl/db_ttl_impl.cc',
    'rocksdb-<(rdbversion)/utilities/write_batch_with_index/write_batch_with_index.cc',
    'rocksdb-<(rdbversion)/utilities/write_batch_with_index/write_batch_with_index_internal.cc',
    'rocksdb-<(rdbversion)/util/event_logger.cc',
    'rocksdb-<(rdbversion)/util/log_buffer.cc',
    'rocksdb-<(rdbversion)/util/logging.cc',
    'rocksdb-<(rdbversion)/util/memenv.cc',
    'rocksdb-<(rdbversion)/util/murmurhash.cc',
    'rocksdb-<(rdbversion)/util/mutable_cf_options.cc',
    'rocksdb-<(rdbversion)/util/options.cc',
    'rocksdb-<(rdbversion)/util/options_builder.cc',
    'rocksdb-<(rdbversion)/util/options_helper.cc',
    'rocksdb-<(rdbversion)/util/options_parser.cc',
    'rocksdb-<(rdbversion)/util/options_sanity_check.cc',
    'rocksdb-<(rdbversion)/util/perf_context.cc',
    'rocksdb-<(rdbversion)/util/perf_level.cc',
    'rocksdb-<(rdbversion)/util/random.cc',
    'rocksdb-<(rdbversion)/util/rate_limiter.cc',
    'rocksdb-<(rdbversion)/util/skiplistrep.cc',
    'rocksdb-<(rdbversion)/util/slice.cc',
    'rocksdb-<(rdbversion)/util/statistics.cc',
    'rocksdb-<(rdbversion)/util/status.cc',
    'rocksdb-<(rdbversion)/util/status_message.cc',
    'rocksdb-<(rdbversion)/util/string_util.cc',
    'rocksdb-<(rdbversion)/util/sync_point.cc',
    'rocksdb-<(rdbversion)/util/thread_local.cc',
    'rocksdb-<(rdbversion)/util/thread_status_impl.cc',
    'rocksdb-<(rdbversion)/util/thread_status_updater.cc',
    'rocksdb-<(rdbversion)/util/thread_status_updater_debug.cc',
    'rocksdb-<(rdbversion)/util/thread_status_util.cc',
    'rocksdb-<(rdbversion)/util/thread_status_util_debug.cc',
    'rocksdb-<(rdbversion)/util/vectorrep.cc',
    'rocksdb-<(rdbversion)/util/xfunc.cc',
    'rocksdb-<(rdbversion)/util/xxhash.cc'

    # 'rocksdb-<(rdbversion)/tools/ldb_cmd.cc',
    # 'rocksdb-<(rdbversion)/tools/ldb_tool.cc',
    # 'rocksdb-<(rdbversion)/tools/sst_dump_tool.cc',

    # 'rocksdb-<(rdbversion)/table/mock_table.cc',
    # 'rocksdb-<(rdbversion)/util/mock_env.cc'
  ]
}]}
